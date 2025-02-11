from fastapi import HTTPException, status, APIRouter
from models import NomeGrupo, Resultado, Numero, TipoOperacao
from utils import obter_logger_e_configuracao


logger = obter_logger_e_configuracao()

router = APIRouter()


@router.get(
    "/teste",
    summary="Retorna mensagem de teste",
    description="Retorna uma mensagem de teste para fins didádicos",
    tags=[NomeGrupo.teste],
)
def hello_world():
    return {"message": "Hello World"}


@router.post("/soma/{numero1}/{numero2}", tags=[NomeGrupo.operacoes])
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


@router.post("/soma2", tags=[NomeGrupo.operacoes])
def soma2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


@router.post(
    path="/soma3",
    response_model=Resultado,
    tags=[NomeGrupo.operacoes],
    status_code=status.HTTP_200_OK,
)
def soma3(numero: Numero):
    total = numero.numero1 + numero.numero2
    return {"resultado": total}


@router.post("/divisao/{numero1}/{numero2}", tags=[NomeGrupo.operacoes])
def divisao(numero1: int, numero2: int):
    if numero2 <= 0:
        raise HTTPException(status_code=400, detail="Não é permitido divisão por zero")

    total = numero1 / numero2

    return {"resultado": total}


@router.post("/operacao", tags=[NomeGrupo.operacoes])
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