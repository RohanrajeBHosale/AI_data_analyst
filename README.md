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
