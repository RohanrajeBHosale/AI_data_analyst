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
2. Install Dependencies
code
Bash
pip install streamlit pandas groq matplotlib seaborn openpyxl python-dotenv
3. Get your API Key
This project uses Groq for free, high-speed inference.
Get your key at: console.groq.com
📂 Project Structure
app.py: The UI and file-loading logic.
analyst.py: The reasoning layer (Language to Python).
executor.py: The execution layer (Local Sandbox).
prompts.py: System instructions.
🖥️ Usage
Run the App:
code
Bash
python3 -m streamlit run app.py
Enter your Groq API Key in the sidebar.
Upload a file (CSV or XLSX).
Ask a question:
"What is the total revenue by category?"
"Clean the sales column and show a trend line."
⚠️ Security Note
This application uses the Python exec() function. While powerful for personal analysis, never use this as a public-facing web application without a secure sandbox (like Docker) to prevent arbitrary code execution.
🗺️ Roadmap

Self-Healing Loop: Auto-fix code errors.

Multi-File Support: Join multiple CSVs.

Clean Data Export: Download the cleaned dataset.
Built with ❤️ using Streamlit, Pandas, and Groq.
code
Code
### Steps on the GitHub Website:
1.  Go to your repository on GitHub.
2.  Click the **"Add file"** button -> **"Create new file"**.
3.  Name it `README.md`.
4.  In the big text box, **Paste** the code from above.
5.  Click the **"Preview"** tab at the top of the editor. It should now look like a professional webpage with bold titles and nice code boxes.
6.  Scroll to the bottom and click the green **"Commit changes..."** button.

That's it! Your project now looks official.
