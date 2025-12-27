from groq import Groq
from prompts import SYSTEM_PROMPT

def ask_llm(user_query, df, api_key):
    """Uses Groq's Llama-3.3 model to generate Python code for free."""
    client = Groq(api_key=api_key)

    # Send column types and a small sample so the AI knows what it's working with
    context = {
        "columns": df.dtypes.astype(str).to_dict(),
        "sample": df.head(3).to_dict(orient='records')
    }

    full_prompt = f"Dataset Context: {context}\nUser Question: {user_query}"

    try:
        completion = client.chat.completions.create(
            # llama-3.3-70b-versatile is excellent for data science tasks
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.1, # Keep it low for consistent code output
        )

        code = completion.choices[0].message.content

        # Strip markdown backticks if the model includes them
        clean_code = code.replace("```python", "").replace("```", "").strip()
        return clean_code

    except Exception as e:
        raise Exception(f"Groq API Error: {str(e)}")