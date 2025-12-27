import streamlit as st
import pandas as pd
import os
from analyst import ask_llm
from executor import run_ai_code

# 1. Page Configuration
st.set_page_config(page_title="AI Data Analyst", layout="wide", page_icon="📊")

# 2. Sidebar for API Key
st.sidebar.header("Configuration")
# Change this line in the sidebar section:
api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

st.title("📊 Personal AI Data Analyst")
st.markdown("""
Upload a messy CSV or Excel file, and ask questions. 
The AI will write the Python code to analyze it and show you the results.
""")

# 3. File Uploader
uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx"])

if uploaded_file:
    # --- Robust Loading Logic (Fixes UnicodeDecodeError) ---
    df = None
    try:
        if uploaded_file.name.endswith('.csv'):
            # Try different encodings
            encodings = ['utf-8', 'latin1', 'utf-16', 'cp1252']
            for enc in encodings:
                try:
                    uploaded_file.seek(0)
                    df = pd.read_csv(uploaded_file, encoding=enc)
                    break
                except (UnicodeDecodeError, pd.errors.ParserError):
                    continue
        else:
            df = pd.read_excel(uploaded_file)

        if df is not None:
            # Clean up column names (removes hidden BOM characters like \ufeff)
            df.columns = df.columns.str.replace('^\\ufeff', '', regex=True).str.strip()

            st.success(f"Successfully loaded '{uploaded_file.name}'")

            # Show Data Preview
            with st.expander("Peek at the Raw Data"):
                st.dataframe(df.head(10))
                st.write(f"**Shape:** {df.shape[0]} rows, {df.shape[1]} columns")
        else:
            st.error("Could not parse the file. Please check the format.")

    except Exception as e:
        st.error(f"Error loading file: {e}")

    # 4. Question Input
    if df is not None:
        st.divider()
        query = st.text_input(
            "What would you like to know?",
            placeholder="e.g., 'Clean the sales column and show me a bar chart of top 5 products by revenue'"
        )

        if query:
            if not api_key:
                st.warning("⚠️ Please provide an OpenAI API Key in the sidebar.")
            else:
                with st.spinner("🧠 AI is reasoning and writing code..."):
                    # 5. Step 1: Generate the Code (Reasoning)
                    try:
                        code = ask_llm(query, df, api_key)

                        # Show the generated code for transparency
                        with st.expander("🛠️ View AI's Python Logic"):
                            st.code(code, language='python')

                        # 6. Step 2: Run the Code (Execution)
                        result = run_ai_code(code, df)

                        # 7. Step 3: Display Results
                        if result["success"]:
                            st.markdown("### 🎯 Analysis Result")
                            st.write(result["answer"])

                            if result["chart"]:
                                st.image(result["chart"])
                                # Optional: Clean up chart file after displaying
                                if os.path.exists(result["chart"]):
                                    os.remove(result["chart"])
                        else:
                            st.error(f"Execution Error: {result['error']}")
                            st.info("The AI might have written code that doesn't match your data. Try re-phrasing.")

                    except Exception as e:
                        st.error(f"AI Logic Error: {e}")

# Footer
st.divider()
st.caption("Built with ❤️ using Streamlit, Pandas, and OpenAI.")