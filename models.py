from pydantic import BaseModel
from enum import Enum


class NomeGrupo(str, Enum):
    """
    Enumeração que representa os nomes dos grupos.

    Atributos:
        teste (str): Retorna o nome do grupo de teste.
        operacoes (str): Retorna o nome do grupo de operações matemáticas.
    """

    teste = "Teste"
    operacoes = "Operações Matemáticas"


class TipoOperacao(str, Enum):
    """
    Enumeração que representa os tipos de operações matemáticas.

    Atributos:
        soma (str): Representa a operação de soma.
        subtracao (str): Representa a operação de subtração.
        multiplicacao (str): Representa a operação de multiplicação.
        divisao (str): Representa a operação de divisão.
    """

    soma = "soma"
    subtracao = "subtracao"
    multiplicacao = "multiplicacao"
    divisao = "divisao"


class Numero(BaseModel):
    """
    Classe Numero que representa um modelo com dois números inteiros.

    Atributos:
        numero1 (int): O primeiro número inteiro.
        numero2 (int): O segundo número inteiro.
    """

    numero1: int
    numero2: int


class Resultado(BaseModel):
    """
    Classe Resultado que herda de BaseModel.

    Atributos:
        resultado (int): Representa o resultado de uma operação ou cálculo.
    """

    resultado: int
