import requests


class APIClient:
    """
    Classe APIClient para interagir com uma API RESTful.
    Métodos:
        __init__(base_url: str, api_token: int):
            Inicializa a classe com a URL base da API e o token de autenticação.
        _get(endpoint: str, params: dict = None):
            Método privado para realizar requisições GET.
        _post(endpoint: str, params: dict = None, json_body: dict = None):
            Método privado para realizar requisições POST.
        teste():
            Retorna uma mensagem de teste.
        soma(numero1: int, numero2: int):
            Realiza a soma de dois números informados na URL.
        soma2(numero1: int, numero2: int):
            Realiza a soma de dois números informados como query params.
        soma3(numero1: int, numero2: int):
            Realiza a soma de dois números enviados no corpo da requisição.
        divisao(numero1: int, numero2: int):
            Realiza a divisão de dois números informados na URL.
        operacao(operacao: str, numero1: int, numero2: int):
            Realiza uma operação matemática específica.
        gerar_historia(tema: str):
            Gera uma história baseada no tema fornecido.
    """

    def __init__(self, base_url: str, api_token: int):
        self.base_url = base_url.rstrip("/")
        self.api_token = api_token

    def _get(self, endpoint: str, params: dict = None):
        params = params or {}
        params["api_token"] = self.api_token
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return response.json()

    def _post(self, endpoint: str, params: dict = None, json_body: dict = None):
        params = params or {}
        params["api_token"] = self.api_token
        response = requests.post(
            f"{self.base_url}{endpoint}", params=params, json=json_body
        )
        return response.json()

    def teste(self):
        """Retorna uma mensagem de teste."""
        return self._get("/operacoes/teste")["mensagem"]

    def soma(self, numero1: int, numero2: int):
        """Realiza a soma de dois números informados na URL."""
        return self._post(f"/operacoes/soma/{numero1}/{numero2}")

    def soma2(self, numero1: int, numero2: int):
        """Realiza a soma de dois números informados como query params."""
        return self._post(
            "/operacoes/soma2", params={"numero1": numero1, "numero2": numero2}
        )

    def soma3(self, numero1: int, numero2: int):
        """Realiza a soma de dois números enviados no corpo da requisição."""
        return self._post(
            "/operacoes/soma3", json_body={"numero1": numero1, "numero2": numero2}
        )["resultado"]

    def divisao(self, numero1: int, numero2: int):
        """Realiza a divisão de dois números informados na URL."""
        return self._post(f"/operacoes/divisao/{numero1}/{numero2}")

    def operacao(self, operacao: str, numero1: int, numero2: int):
        """Realiza uma operação matemática específica."""
        return self._post(
            "/operacoes/operacao",
            params={"operacao": operacao},
            json_body={"numero1": numero1, "numero2": numero2},
        )

    def gerar_historia(self, tema: str):
        """Gera uma história baseada no tema fornecido."""
        return self._post("/llm/gerar_historia", params={"tema": tema})
