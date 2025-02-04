from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Primeira rota ou primeiro Endpoint
@app.get("/teste")
def hello_world():
    return {"message": "Hello World"}

# Criando um Endpoint para receber dois números e mostrar a som dos dois
@app.post("/soma/{numero1}/{numero2}") 
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}

# Formato2 - Recebendo os números como parâmetros
@app.post("/soma2")
def soma2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}

# Formato3 - Recebendo os números no corpo da requisição
class Numero(BaseModel):
    numero1: int
    numero2: int
    numero3: int = 0
    
@app.post("/soma3")
def soma3(numero: Numero):
    total = numero.numero1 + numero.numero2 + numero.numero3
    return {"resultado": total}
