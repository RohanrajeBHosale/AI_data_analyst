import pandas as pd
import matplotlib.pyplot as plt
import os

def run_ai_code(code, df):
    """Executes the AI code and returns the result."""
    # Reset plot if any exist
    plt.clf()

    # Environment for execution
    local_vars = {"df": df, "pd": pd, "plt": plt}

    try:
        exec(code, {}, local_vars)

        # Check if code generated a chart
        chart_path = "temp_chart.png"
        has_chart = os.path.exists(chart_path)

        return {
            "success": True,
            "answer": local_vars.get("result_text", "Code executed but result_text not set."),
            "chart": chart_path if has_chart else None
        }
    except Exception as e:
        return {"success": False, "error": str(e)}