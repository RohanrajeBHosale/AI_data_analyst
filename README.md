
Here is a clean, professional README.md file designed for your project. You can save this text directly into a file named README.md in your project folder.
📊 Personal AI Data Analyst
Stop asking AI to do the math. Start asking AI to write the code.
This project is a local-first AI data analysis tool. It solves the biggest problem with LLMs in data science: Hallucinations. Instead of asking an AI to calculate averages or trends (which it often gets wrong), this tool uses the AI as a "Senior Data Analyst" that writes precise Python code to perform the work on your local machine using Pandas and Matplotlib.
🧠 The Philosophy
Privacy First: Your raw data never leaves your machine. Only the column names and a small sample of types are sent to the AI.
Accuracy: Calculations are performed by Python’s computational engine, not the LLM’s linguistic engine.
Speed: Powered by Groq (Llama 3.3 70B) for near-instantaneous code generation.
🚀 Features
Messy Data Handling: Robust loading logic that automatically handles UnicodeDecodeError and hidden BOM characters from Excel exports.
Natural Language to Code: Converts "Show me a bar chart of top 5 categories" into executable Pandas/Matplotlib logic.
Local Execution: Runs code in a local environment, allowing for analysis of large files that would exceed LLM token limits.
Automated Visualization: Automatically detects when a chart is requested and renders it within the UI.
🛠️ Tech Stack
Frontend: Streamlit
Reasoning Engine: Groq API (Llama 3.3 70B Versatile)
Data Processing: Pandas
Visualization: Matplotlib & Seaborn
⚙️ Installation & Setup
1. Prerequisites
Ensure you have Python 3.9+ installed.
2. Clone and Initialize
code
Bash
git clone https://github.com/yourusername/ai-data-analyst.git
cd ai-data-analyst
3. Set Up Virtual Environment
code
Bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
4. Install Dependencies
code
Bash
pip install streamlit pandas groq matplotlib seaborn openpyxl python-dotenv
📂 Project Structure
app.py: The main UI, file uploader, and robust data loading logic.
analyst.py: The brain. Formats the data metadata and communicates with the Groq API.
executor.py: The sandbox. Safely executes AI-generated code and captures outputs/charts.
prompts.py: System prompts that enforce strict "Python-only" output from the AI.
🖥️ Usage
Launch the app:
code
Bash
streamlit run app.py
Configuration: Enter your Groq API Key in the sidebar.
Upload: Drop in any CSV or Excel file (even messy ones!).
Query: Ask questions like:
"What are the top 5 products by revenue?"
"Clean the Sales column by removing dollar signs and commas, then show a trend line."
"Identify outliers in the price column using z-score."
🛡️ Security Note
This application uses Python's exec() function to run AI-generated code locally.
Personal Use: Safe for local data analysis on your own machine.
Production: Do not host this as a public web application without implementing a secure sandbox (like E2B, Pyodide, or Docker containers) to prevent malicious code execution.
🗺️ Roadmap

Self-Healing Loop: If the code fails, the error is sent back to the AI for an automatic fix.

Multi-File Chat: Support for merging and analyzing multiple CSVs at once.

Clean Data Export: One-click button to download the dataset after the AI cleans it.
Built to make data science accessible through the power of Code-as-Action.
