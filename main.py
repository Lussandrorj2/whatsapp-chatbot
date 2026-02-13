from fastapi import FastAPI, Request
import requests
import os
from dotenv import load_dotenv
from llm import ask_llm

load_dotenv()

app = FastAPI()

WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


@app.get("/webhook")
async def verify_webhook(mode: str = None, verify_token: str = None, challenge: str = None):
    if mode == "subscribe" and verify_token == VERIFY_TOKEN:
        return int(challenge)
    return {"error": "Verification failed"}


@app.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        sender = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]

        ai_response = ask_llm(message)

        send_whatsapp_message(sender, ai_response)

    except Exception as e:
        print("Erro:", e)

    return {"status": "ok"}


def send_whatsapp_message(to, message):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message},
    }

    requests.post(url, headers=headers, json=data)

#rota temporaria 

@app.get("/test")
def test():
    return {"resposta": ask_gemini("Explique IA em 1 linha")}
