# 📊 Personal AI Data Analyst

**"Don't ask the AI to do the math. Ask the AI to write the code that does the math."**

This is a local AI-powered data science tool that allows you to chat with messy CSV/Excel files. Instead of sending your entire dataset to a cloud LLM, this tool sends only the **metadata** (schema). The AI then reasons about your question, writes functional Python/Pandas code, and executes it locally on your machine to provide deterministic, accurate answers and visualizations.

---

## 🚀 Features

- **Privacy-First Architecture:** Your raw data stays on your machine. Only column names and sample types are sent to the LLM.
- **Deterministic Accuracy:** Leverages the computational precision of Pandas and Matplotlib rather than relying on LLM "hallucinated" calculations.
- **Robust Data Ingestion:** Automatically handles common encoding issues (`UnicodeDecodeError`) and hidden BOM characters from Excel.
- **Interactive Visualizations:** Generates charts (Matplotlib/Seaborn) based on natural language requests.
- **Ultra-Fast Inference:** Powered by **Groq** (Llama 3.3 70B) for near-instant code generation.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Intelligence:** [Groq](https://groq.com/) (Llama 3.3 70B Versatile)
- **Data Engine:** [Pandas](https://pandas.pydata.org/)
- **Visuals:** [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/)

---

## ⚙️ Setup & Installation

### 1. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows
```

2. Install Dependencies
code
Bash
pip install streamlit pandas groq matplotlib seaborn openpyxl python-dotenv
3. Get your API Key
This project is configured to use Groq for free, high-speed inference.
Get your free key at: console.groq.com
📂 Project Structure
app.py: The Streamlit UI and robust file-loading logic.
analyst.py: The "Reasoning" layer that converts natural language to Python via Groq.
executor.py: The "Execution" layer that runs generated code in a local sandbox.
prompts.py: The system instructions that enforce strict Python-only output.
🖥️ Usage
Run the App:
code
Bash
python3 -m streamlit run app.py
Enter your Groq API Key in the sidebar.
Upload a file (CSV or XLSX).
Ask a question:
"What is the total revenue by category?"
"Clean the sales column (remove $ and commas) and show a trend line."
"Who are the top 5 customers by order volume?"
⚠️ Security Note
This application uses the Python exec() function to run AI-generated code. While this is powerful for personal data analysis, never use this as a public-facing web application without implementing a secure sandbox (like Docker or E2B) to prevent arbitrary code execution.
🗺️ Roadmap

Self-Healing Loop: Automatically send errors back to the AI for a second attempt.

Multi-File Support: Join multiple CSVs for complex relational analysis.

Clean Data Export: One-click button to download the dataset after the AI cleans it.
Built with ❤️ using Streamlit, Pandas, and Groq.
