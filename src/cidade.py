from typing import List


class Cidade:
    def __init__(
        self,
        nome: str,
        custo: int,
        adjascentes: List = [],
        visitado: bool = False,
    ) -> None:
        self.nome = nome
        self.custo = custo
        self.adjascentes = adjascentes
        self.visitado = visitado


class Adjascente:
    def __init__(self, cidade_destino: Cidade, custo_do_caminho: int):
        self.cidade_destino = cidade_destino
        self.custo_do_caminho = custo_do_caminho
