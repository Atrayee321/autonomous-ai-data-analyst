<div align="center">

# 📊 Autonomous AI Data Analyst

### Transform Raw Data into Actionable Insights with Agentic AI

**An intelligent, dataset-independent AI-powered analytics application.**

Upload datasets • Explore insights • Ask questions • Generate reports

[![Launch Live App](https://img.shields.io/badge/🚀_Launch_Live_App-Streamlit-FF4B4B?style=for-the-badge)](https://autonomous-ai-data-analyst-kmbpc8frppj6wdhroqziof.streamlit.app/)

**🌐 [Try the Live Application](https://autonomous-ai-data-analyst-kmbpc8frppj6wdhroqziof.streamlit.app/)**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_AI-purple)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white)

**[Live Demo](#-live-demo) • [Features](#-key-features) • [Architecture](#-system-architecture) • [Installation](#-getting-started) • [Deployment](#-deployment)**

</div>

---

## 🌟 About the Project

**Autonomous AI Data Analyst** is an agentic Generative AI application designed to simplify exploratory data analysis, business intelligence, and natural-language data exploration.

Built using **Google Gemini, LangGraph, Pandas, Plotly, and Streamlit**, the application combines AI-driven planning with Python-based analytical tools.

Instead of manually writing analytical code for every question, users can upload a dataset and let the AI plan appropriate analyses or answer questions about the data.

> **Project Status:** Functional prototype under development. AI-generated explanations should be verified before making important decisions.

---

## 🌐 Live Demo

Experience the Autonomous AI Data Analyst through the deployed Streamlit application.

### 🚀 [Launch Autonomous AI Data Analyst](https://autonomous-ai-data-analyst-kmbpc8frppj6wdhroqziof.streamlit.app/)

> **Note:** Access to the application depends on its Streamlit sharing settings. The application uses Gemini API quotas, so availability may vary.

---

## 🚀 Key Features

### 🤖 1. Autonomous Data Analysis

- Automatically profiles uploaded datasets.
- Identifies numerical, categorical, and date columns.
- Uses Gemini to select relevant analytical tools.
- Executes validated Pandas operations through LangGraph.
- Generates analytical findings and business intelligence reports.

### 💬 2. Ask Your Data

- Ask questions in natural language.
- Supports multi-part analytical questions.
- Automatically breaks questions into smaller tasks.
- Executes analytical tools using Python.
- Generates evidence-based responses.

**Example questions:**

- Which category has the highest total sales?
- Which department has the highest average salary?
- How have monthly sales changed over time?
- Which category has the highest sales and which has the highest average profit?

### 📈 3. Data Visualization

- Interactive Plotly charts.
- Bar charts for grouped comparisons.
- Line charts for supported time-series analyses.
- Dataset-aware visualization selection.

### 🔍 4. Universal Dataset Profiling

- Dataset dimensions and column types.
- Missing-value detection.
- Duplicate-row identification.
- Numerical summary statistics.
- Categorical frequency analysis.
- Date-column identification.

### 📄 5. Business Intelligence Reporting

- AI-generated analytical summaries.
- Key findings and recommendations.
- Transparent analytical evidence.
- Downloadable Markdown reports.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Google Gemini** | AI planning and natural-language explanations |
| **LangGraph** | Agent workflow orchestration |
| **Pandas** | Data manipulation and analytical calculations |
| **NumPy** | Numerical processing |
| **Plotly** | Interactive visualizations |
| **Streamlit** | Web application interface |
| **GitHub** | Version control |
| **Streamlit Community Cloud** | Application deployment |

---

## 🧠 System Architecture

```text
             USER
               |
               v
       Upload CSV / Excel
               |
               v
       Dataset Profiling
               |
               v
        Select AI Mode
               |
        +------+------+
        |             |
        v             v
   Autonomous      Ask Your
    Analysis         Data
        |             |
        v             v
   Gemini Agent    Question
    Planning       Planning
        |             |
        v             v
   LangGraph       Multi-Step
    Workflow       Tool Execution
        |             |
        +------+------+
               |
               v
      Pandas Analytical Tools
               |
               v
       Verified Computations
               |
               v
       Gemini Explanation
               |
               v
       Insights & Reports
```

The AI selects predefined operations, while Pandas performs the actual calculations. The application does not execute arbitrary AI-generated Python code.

---

## 📁 Project Structure

```text
autonomous-ai-data-analyst/
│
├── app.py
├── analyst_engine.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── .streamlit/
│   └── config.toml
│
├── tests/
│   └── test_tools.py
│
└── Autonomous_AI_Data_Analyst.ipynb
```

The Jupyter notebook contains the original Google Colab development experiments. The Streamlit application uses the separate Python modules.

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Atrayee321/autonomous-ai-data-analyst.git
cd autonomous-ai-data-analyst
```

The repository is private, so GitHub access is required.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Obtain an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a local `.streamlit/secrets.toml` file:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

> 🔐 Never commit actual API keys to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

Upload a CSV or Excel dataset and select your preferred analysis mode.

---

## ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

**Live App:** [Autonomous AI Data Analyst](https://autonomous-ai-data-analyst-kmbpc8frppj6wdhroqziof.streamlit.app/)

To deploy your own instance:

1. Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Connect your GitHub account and authorize repository access.
3. Select the repository containing the application.
4. Choose the `main` branch.
5. Set the main file path to `app.py`.
6. Add `GEMINI_API_KEY` under **App Settings → Secrets**.
7. Deploy and test both analysis modes.

**Security:** Keep API credentials in Streamlit Secrets and configure app-sharing permissions separately from repository visibility.

---

## 🧪 Testing

Run the basic analytical tool tests using:

```bash
pip install pytest
pytest -q
```

These tests cover selected Python analytical operations. End-to-end application and AI-response validation are still being developed.

---

## ⚠️ Current Limitations

- Designed for general-purpose tabular data, not every file type or analytical task.
- Supports CSV and XLSX uploads up to 15 MB.
- Multi-step questions support up to five analytical tasks.
- Some advanced mathematical and domain-specific questions are not yet supported.
- Grouped results and time-series outputs are limited for performance.
- AI-generated explanations may contain errors even when underlying Python calculations are correct.
- Free-tier API quotas and hosting limits may change.

---

## 🔮 Future Enhancements

- [x] Universal dataset profiling
- [x] Autonomous analytical planning
- [x] LangGraph agent workflow
- [x] Multi-step natural-language question answering
- [x] Interactive Streamlit dashboard
- [x] CSV and Excel support
- [ ] Advanced visualization options
- [ ] Automatic analytical error recovery
- [ ] Stronger numerical verification
- [ ] Automated PDF report generation
- [ ] Additional analytical tools
- [ ] Improved large-dataset support
- [ ] Persistent analysis history

---

## 🎯 Project Objective

To make data analysis more accessible by creating an intelligent AI assistant that can understand datasets, select appropriate analytical tools, perform computations, and communicate useful insights in natural language.

---

<div align="center">

### ⭐ Built with Python, Gemini, LangGraph & Streamlit

**Turning data into insights, one question at a time.**

### 🚀 [Try the Live App](https://autonomous-ai-data-analyst-kmbpc8frppj6wdhroqziof.streamlit.app/)

</div>

### ⭐ Built with Python, Gemini, LangGraph & Streamlit

**Turning data into insights, one question at a time.**

</div>

