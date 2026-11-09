import pandas as pd
from analyst_engine import execute_tool, profile_dataset, execute_plan


def sample():
    return pd.DataFrame({
        "Department": ["A", "B", "A", "B"],
        "Salary": [10, 20, 30, 40],
        "Date": ["2024-01-01", "2024-01-02", "2024-02-01", "2024-02-02"],
    })


def test_generic_profile():
    p = profile_dataset(sample())
    assert p["rows"] == 4
    assert "Salary" in p["numeric_columns"]
    assert "Date" in p["date_columns"]


def test_grouped_tool():
    result = execute_tool(sample(), "grouped_analysis", {
        "category_col": "Department",
        "numeric_col": "Salary",
        "operation": "mean",
    })
    assert result["values"] == {"B": 30.0, "A": 20.0}


def test_multi_tool_plan():
    plan = {"tasks": [
        {"selected_tool": "data_quality", "parameters": {}},
        {"selected_tool": "summary_statistics", "parameters": {}},
    ]}
    results = execute_plan(sample(), plan)
    assert len(results) == 2
    assert all(x["result"]["status"] == "success" for x in results)
