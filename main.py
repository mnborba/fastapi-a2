from fastapi import FastAPI, status, HTTPException, Depends
from pydantic import BaseModel
from enum import Enum
import logging
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="[%(levelname)s] %(asctime)s: %(message)s"
)
logger = logging.getLogger("fastapi")

NOME_GRUPO_TESTE = "Teste"
NOME_GRUPO_OPERACOES = "Operações Matemáticas Top"


class NomeGrupo(str, Enum):
    teste = "Teste"
    operacoes = "Operações Matemáticas"


API_TOKEN = 123456


def common_verificacao_api_token(api_token: int):
    if api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="API Token inválido")


descricao = """ 
    API desenvolvida durante a aula 2, com exemplos de soma. 
    
    # Rotas definidas 
    - /teste: retorna uma mensagem de sucesso 
    - /soma/numero1/numero2:  recebe dois números e retorna a soma 
"""

app = FastAPI(
    title="FastAPI Aula 2",
    description=descricao,
    version="4.3",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Marcelo Nunes Borba",
        "url": "http://github.com/mnborba/",
        "email": "marceloborba@discente.ufg.br",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    dependencies=[Depends(common_verificacao_api_token)],
)


# Primeira rota ou primeiro Endpoint
@app.get(
    "/teste",
    summary="Retorna mensagem de teste",
    description="Retorna uma mensagem de teste para fins didádicos",
    tags=[NomeGrupo.teste],
)
def hello_world():
    return {"message": "Hello World"}


# Criando um Endpoint para receber dois números e mostrar a som dos dois
@app.post("/soma/{numero1}/{numero2}", tags=[NomeGrupo.operacoes])
def soma(numero1: int, numero2: int, api_token: int):
    logger.info(f"API Token recebido: {api_token}")
    logger.info(f"Requisição recebida: Numero1: {numero1} e Número2: {numero2}")

    if numero1 < 0 or numero2 < 0:
        logger.error("ERRO: Não permitido Número negativo")
        raise HTTPException(status_code=400, detail="Não é permitido números negativos")

    total = numero1 + numero2

    if total < 0:
        logger.error("ERRO: Não permitido resultado negativo")
        raise HTTPException(
            status_code=400, detail="O resultado da soma não pode ser negativo"
        )

    logger.info(f"Requisição processada com SUCESSO!!!  Resultado da soma: {total}")

    return {
        "resultado": total,
        "WARNING": "Esta versão de Endpoint será descontinuada em 30 dias",
    }


# Formato2 - Recebendo os números como parâmetros
@app.post("/soma2", tags=[NomeGrupo.operacoes])
def soma2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# Formato3 - Recebendo os números no corpo da requisição
class Numero(BaseModel):
    numero1: int
    numero2: int


class Resultado(BaseModel):
    resultado: int


# Primeira forma de definir o modelo do Resultado   - MAIS INDICADO
@app.post(
    path="/soma3",
    response_model=Resultado,
    tags=[NomeGrupo.operacoes],
    status_code=status.HTTP_200_OK,
)
def soma3(numero: Numero):
    total = numero.numero1 + numero.numero2
    return {"resultado": total}


# Criando um Endpoint para receber dois números e mostrar a som dos dois
@app.post("/divisao/{numero1}/{numero2}", tags=[NomeGrupo.operacoes])
def divisao(numero1: int, numero2: int):
    if numero2 <= 0:
        raise HTTPException(status_code=400, detail="Não é permitido divisão por zero")

    total = numero1 / numero2

    return {"resultado": total}


class TipoOperacao(str, Enum):
    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"


@app.post("/operacao", tags=[NomeGrupo.operacoes])
def operacao(numeros: Numero, operacao: TipoOperacao):
    if operacao == TipoOperacao.soma:
        resultado = numeros.numero1 + numeros.numero2

    elif operacao == TipoOperacao.subtracao:
        resultado = numeros.numero1 - numeros.numero2

    elif operacao == TipoOperacao.multiplicacao:
        resultado = numeros.numero1 * numeros.numero2

    elif operacao == TipoOperacao.divisao:
        resultado = numeros.numero1 / numeros.numero2

    return {"resultado": resultado}


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


@app.post("/gerar_historia")
def gerar_historia(tema: str):
    historia = executar_prompt(tema)

    return {"Historia": historia}
