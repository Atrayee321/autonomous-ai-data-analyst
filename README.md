# Autonomous AI Data Analyst

A **dataset-independent, single-agent AI analytics prototype** built with **Streamlit, Google Gemini, LangGraph, Pandas, and Plotly**.

> Status: early working prototype. The original Google Colab experiments are preserved in `Autonomous_AI_Data_Analyst.ipynb`. The deployable application is implemented separately in `app.py` and `analyst_engine.py`. Numerical findings and model-written reports must be reviewed before important decisions.

## Features

- **Autonomous Analysis:** inspect schema and data quality, let Gemini select appropriate validated analytical tools, execute them with Pandas through a bounded LangGraph loop, generate a chart when appropriate, and write a business intelligence report.
- **Ask Your Data:** answer natural-language questions using up to five validated analysis tasks with transparent tool results. The model cannot execute arbitrary Python.
- **Data uploads:** CSV and XLSX, 15 MB demo limit; one active dataset per user session.
- **Generic analytics:** data quality, summary statistics, categorical frequencies, grouped aggregation, and time-series analysis.
- **Evidence visibility:** users can expand executed tool results to inspect the computed evidence.

## Project layout

```text
app.py                         Streamlit interface (two modes)
analyst_engine.py              Dataset-scoped tools and Gemini/LangGraph workflow
requirements.txt               Application dependencies
.streamlit/config.toml         Streamlit configuration
.env.example                   Placeholder for local API configuration (no secrets)
.gitignore                     Excludes local secrets/data and generated files
tests/test_tools.py            Basic deterministic tests
Autonomous_AI_Data_Analyst.ipynb  Original Colab development notebook
```

## Setup (local)

1. Install Python 3.11 or 3.12.
2. Create a virtual environment and activate it.
3. Run `pip install -r requirements.txt`.
4. Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).
5. Provide the key as an environment variable named `GEMINI_API_KEY`, or put it in a local **untracked** file `.streamlit/secrets.toml`:

   ```toml
   GEMINI_API_KEY = "your_key_here"
   ```

6. Run `streamlit run app.py`.

**Never commit your actual Gemini API key, datasets containing private information, or Colab outputs with secrets.**

## Deploy free on Streamlit Community Cloud

1. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Choose **Create app** and select this GitHub repository and the `main` branch. GitHub integration must have access to this private repository.
3. Set **Main file path** to `app.py`.
4. Under **Advanced settings → Secrets**, add:

   ```toml
   GEMINI_API_KEY = "your_key_here"
   ```

5. Deploy. The Gemini API must have quota for `gemini-3.1-flash-lite` in your account. Free service tiers have changing rate and resource limits.

**Privacy:** A private GitHub repository does not make a deployed app private by itself. Configure Streamlit app access separately if needed. Users' uploaded datasets are not stored in the repo, and the app avoids globally shared DataFrames. Data summaries and computed results are sent to Google's Gemini API; follow its current data-handling policy. Do not use sensitive datasets without appropriate authorization.

## Tests

```bash
pip install pytest
pytest -q
```

## Limitations

- General-purpose **tabular** data only; unusual formats, ambiguous dates, empty or unsupported columns, and some domain-specific questions may not work.
- The planner may select invalid tool parameters; the executor rejects unsupported choices. This prototype does not automatically repair all failed plans.
- Multi-step Q&A supports up to five tool operations; derived financial measures are not inferred automatically.
- Grouped tools return the top 20 groups; the time-series tool limits output to 36 periods.
- Charting currently covers validated bar and line aggregations, not every plot type.
- Model-written insights are generated from computed evidence but are **not a formal guarantee of numerical correctness**.
- No multi-user persistent history or database. Conversation history lasts for the current Streamlit session and is cleared when the dataset changes.
- For production, add quotas, stronger data privacy, error recovery, schema validation, numerical claim verification, more tests, and authentication/access controls.

## Original architecture

```text
Upload CSV/XLSX
    ↓
Pandas dataset profile
    ↓
┌────────────────────────────┬──────────────────────────────┐
│ Autonomous Analysis        │ Ask Your Data                │
│ Gemini plan → Pandas tool  │ Question → Gemini task plan  │
│   ↳ LangGraph loop         │ → Pandas tools → AI response │
└────────────────────────────┴──────────────────────────────┘
    ↓
Plotly chart + evidence + BI report (as applicable)
```

**Stack:** Python • Pandas • NumPy • Plotly • Streamlit • LangGraph • google-genai.
