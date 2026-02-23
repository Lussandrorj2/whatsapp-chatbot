import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def ask_llm(text: str):
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=text
        )

        print("Resposta Gemini:", response.text)
        return response.text

    except Exception as e:
        print("Erro Gemini:", e)
        return "Erro interno no processamento."