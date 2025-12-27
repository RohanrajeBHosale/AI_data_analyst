# 📊 Personal AI Data Analyst

**"Don't ask the AI to do the math. Ask the AI to write the code that does the math."**

This is a local AI-powered data science tool that allows you to chat with messy CSV/Excel files. This tool sends only the **metadata** (schema) to the AI, which then writes Python/Pandas code and executes it locally to provide accurate answers and charts.

---

## 🚀 Features

* **Privacy-First:** Your raw data stays on your machine.
* **Deterministic Accuracy:** Calculations are performed by Pandas, not the LLM.
* **Robust Ingestion:** Handles encoding issues and hidden BOM characters automatically.
* **Interactive Visuals:** Generates Matplotlib/Seaborn charts from natural language.
* **Ultra-Fast:** Powered by **Groq (Llama 3.3 70B)**.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Intelligence:** Groq (Llama 3.3 70B)
* **Data Engine:** Pandas
* **Visuals:** Matplotlib / Seaborn

---

## ⚙️ Setup & Installation

### 1. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 2. Install Dependencies
pip install streamlit pandas groq matplotlib seaborn openpyxl python-dotenv


### 3. Get your API Key
This project uses Groq for free, high-speed inference.
Get your key at: console.groq.com


## 📂 Project Structure
app.py: The UI and file-loading logic.
analyst.py: The reasoning layer (Language to Python).
executor.py: The execution layer (Local Sandbox).
prompts.py: System instructions.

## 🖥️ Usage
1.Run the App:
```
python3 -m streamlit run app.py
```
2.Enter your Groq API Key in the sidebar.
3.Upload a file (CSV or XLSX).
4.Ask a question:
-"What is the total revenue by category?"
-"Clean the sales column and show a trend line."

## ⚠️ Security Note
This application uses the Python exec() function. While powerful for personal analysis, never use this as a public-facing web application without a secure sandbox (like Docker) to prevent arbitrary code execution.

## 🗺️ Roadmap

Self-Healing Loop: Auto-fix code errors.

Multi-File Support: Join multiple CSVs.

Clean Data Export: Download the cleaned dataset.


