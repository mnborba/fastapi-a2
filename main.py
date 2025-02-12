from fastapi import FastAPI, Depends
from utils import common_verificacao_api_token
from routers import llm_router, operacoes_router


descricao = """ 
    API desenvolvida durante a aula 2, com exemplos de soma. 
    
    # Rotas definidas 
    - /teste: retorna uma mensagem de sucesso 
    - /soma/numero1/numero2:  recebe dois números e retorna a soma 
"""


app = FastAPI(
    title="FastAPI Aula 3",
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

app.include_router(operacoes_router.router, prefix="/operacoes")
app.include_router(llm_router.router, prefix="/llm")