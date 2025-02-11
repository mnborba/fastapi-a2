from fastapi import HTTPException
from groq import Groq
import os
import logging
from dotenv import load_dotenv


load_dotenv()


API_TOKEN = int(os.getenv("API_TOKEN"))


def obter_logger_e_configuracao():
    logging.basicConfig(
        level=logging.INFO, format="[%(levelname)s] %(asctime)s: %(message)s"
    )
    logger = logging.getLogger("fastapi")
    return logger


def common_verificacao_api_token(api_token: int):
    if api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="API Token inválido")


def executar_prompt(tema: str):
    prompt = f"Escreva uma historia sobre {tema}, em no máximo 5 linhas."

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content