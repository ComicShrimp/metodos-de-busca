from typing import List


class Cidade:
    nome: str
    visitado: bool
    adjascentes: List = []

    def __init__(
        self,
        nome: str,
        adjascentes: List = [],
        visitado: bool = False,
    ) -> None:
        self.nome = nome
        self.adjascentes = adjascentes
        self.visitado = visitado
