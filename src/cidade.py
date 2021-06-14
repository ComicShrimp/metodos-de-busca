from typing import List, TYPE_CHECKING


class Cidade:
    nome: str
    visitado: bool
    cidades_adjascentes: List

    def __init__(
        self, nome: str, cidades_adjascentes: List, visitado: bool = False
    ) -> None:
        self.nome = nome
        self.visitado = visitado
        self.cidades_adjascentes = cidades_adjascentes
