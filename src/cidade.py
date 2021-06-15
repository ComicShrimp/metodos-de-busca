from typing import List


class Cidade:
    def __init__(
        self,
        nome: str,
        adjascentes: List = [],
        visitado: bool = False,
    ) -> None:
        self.nome = nome
        self.adjascentes = adjascentes
        self.visitado = visitado


class adjascente:
    cidade_destino: Cidade
    custo__do_caminho: int
