"""Streamlit UI for the Autonomous AI Data Analyst."""
from __future__ import annotations

import hashlib
import io
import os

import pandas as pd
import plotly.express as px
import streamlit as st
from google import genai

from analyst_engine import answer_question, autonomous_analysis, profile_dataset

st.set_page_config(page_title="Autonomous AI Data Analyst", page_icon="📊", layout="wide")
st.title("📊 Autonomous AI Data Analyst")
st.caption("Dataset-aware agentic analysis • Gemini + LangGraph + Pandas + Plotly")

MAX_UPLOAD_BYTES = 15 * 1024 * 1024


def get_api_key() -> str | None:
    try:
        secret = st.secrets.get("GEMINI_API_KEY")
        if secret:
            return str(secret)
    except (FileNotFoundError, KeyError):
        pass
    return os.getenv("GEMINI_API_KEY")


def load_dataset(file) -> pd.DataFrame:
    raw = file.getvalue()
    if len(raw) > MAX_UPLOAD_BYTES:
        raise ValueError("File exceeds the 15 MB demonstration limit.")
    if file.name.lower().endswith(".csv"):
        try:
            data = pd.read_csv(io.BytesIO(raw))
        except UnicodeDecodeError:
            data = pd.read_csv(io.BytesIO(raw), encoding="latin-1")
    elif file.name.lower().endswith(".xlsx"):
        data = pd.read_excel(io.BytesIO(raw))
    else:
        raise ValueError("Only CSV and XLSX uploads are supported.")
    if data.empty:
        raise ValueError("The uploaded dataset contains no rows.")
    if data.columns.duplicated().any():
        raise ValueError("Duplicate column names are not supported.")
    if len(data.columns) > 150:
        raise ValueError("This demo supports at most 150 columns.")
    return data


def show_chart(df: pd.DataFrame, spec: tuple[str, str, str] | None) -> None:
    if not spec:
        return
    chart_type, x, y = spec
    if x not in df or y not in df or not pd.api.types.is_numeric_dtype(df[y]):
        return
    try:
        if chart_type == "bar":
            grouped = df.groupby(x, dropna=False)[y].sum().nlargest(20).reset_index()
            fig = px.bar(grouped, x=x, y=y, title=f"Total {y} by {x}")
        elif chart_type == "line":
            dates = pd.to_datetime(df[x], errors="coerce", format="mixed")
            view = pd.DataFrame({"date": dates, y: df[y]}).dropna(subset=["date"])
            if view.empty:
                return
            grouped = view.groupby("date", as_index=False)[y].sum().sort_values("date")
            fig = px.line(grouped, x="date", y=y, title=f"{y} over time")
        else:
            return
        st.plotly_chart(fig, use_container_width=True)
    except (ValueError, TypeError) as exc:
        st.warning(f"Chart unavailable: {exc}")


api_key = get_api_key()
if not api_key:
    st.warning("Add GEMINI_API_KEY to Streamlit secrets before running AI analysis.")

uploaded = st.file_uploader("Upload your CSV or Excel dataset", type=["csv", "xlsx"])
if uploaded is None:
    st.info("Upload a dataset to begin. Your dataset is analyzed within this app session.")
    st.stop()

try:
    df = load_dataset(uploaded)
except (ValueError, pd.errors.ParserError, OSError) as exc:
    st.error(f"Unable to load dataset: {exc}")
    st.stop()

file_digest = hashlib.sha256(uploaded.getvalue()).hexdigest()
if st.session_state.get("dataset_digest") != file_digest:
    st.session_state["dataset_digest"] = file_digest
    st.session_state["analysis_result"] = None
    st.session_state["qa_history"] = []

profile = profile_dataset(df)
c1, c2, c3 = st.columns(3)
c1.metric("Rows", f"{len(df):,}")
c2.metric("Columns", len(df.columns))
c3.metric("Missing cells", f"{df.isna().sum().sum():,}")
with st.expander("Preview and dataset structure", expanded=True):
    st.dataframe(df.head(20), use_container_width=True)
    st.json(profile, expanded=False)

mode = st.radio("Choose mode", ["Autonomous Analysis", "Ask Your Data"], horizontal=True)
if mode == "Autonomous Analysis":
    if st.button("Run autonomous analysis", type="primary", disabled=not bool(api_key)):
        with st.spinner("Gemini is planning; Python is computing..."):
            try:
                result = autonomous_analysis(df, genai.Client(api_key=api_key))
                st.session_state["analysis_result"] = result
            except Exception as exc:
                st.error(f"Analysis failed: {exc.__class__.__name__}: {exc}")
    result = st.session_state.get("analysis_result")
    if result:
        st.subheader("Analytical evidence")
        for item in result["results"]:
            with st.expander(item.get("tool", "Analysis")):
                st.json(item, expanded=False)
        show_chart(df, result.get("chart"))
        st.subheader("Business intelligence report")
        st.markdown(result["report"])
        st.download_button("Download report (.md)", result["report"],
                           file_name="business_intelligence_report.md", mime="text/markdown")
else:
    st.subheader("Ask questions about the uploaded dataset")
    for entry in st.session_state.get("qa_history", []):
        with st.chat_message("user"):
            st.write(entry["question"])
        with st.chat_message("assistant"):
            st.markdown(entry["answer"])
    question = st.chat_input("For example: Which category has the highest average value?",
                             disabled=not bool(api_key))
    if question:
        with st.spinner("Planning and executing analytical tools..."):
            try:
                result = answer_question(df, genai.Client(api_key=api_key), question)
                st.session_state["qa_history"].append({"question": question, "answer": result["answer"]})
                with st.chat_message("user"):
                    st.write(question)
                with st.chat_message("assistant"):
                    st.markdown(result["answer"])
                    with st.expander("Tool execution and evidence"):
                        st.json({"plan": result["plan"], "results": result["results"]}, expanded=False)
                    show_chart(df, result.get("chart"))
            except Exception as exc:
                st.error(f"Question could not be answered: {exc.__class__.__name__}: {exc}")

st.caption("Prototype only: AI explanations can be inaccurate; verify high-stakes findings. "
           "Uploads are processed in this session; do not upload sensitive data to a free-tier AI API.")
