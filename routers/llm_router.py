from fastapi import APIRouter
from utils import obter_logger_e_configuracao, executar_prompt



logger = obter_logger_e_configuracao()

router = APIRouter()


@router.post("/gerar_historia")
def gerar_historia(tema: str):
    historia = executar_prompt(tema)

    return {"Historia": historia}