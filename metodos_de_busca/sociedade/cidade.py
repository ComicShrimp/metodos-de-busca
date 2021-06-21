from typing import List


class Cidade:
    def __init__(
        self,
        nome: str,
        custo: int,
        vizinhos: List = [],
        visitado: bool = False,
    ) -> None:
        self.nome = nome
        self.custo = custo
        self.vizinhos = vizinhos
        self.visitado = visitado

    def visitar(self):
        self.visitado = True

    def foi_visitado(self) -> bool:
        return self.visitado

    def reiniciar_visitado(self):
        self.visitado = False

    def eh_igual(self, cidade):
        return cidade.nome == self.nome

    def __str__(self) -> str:
        return self.nome

    def __repr__(self) -> str:
        return self.nome


class Vizinho:
    def __init__(self, cidade_destino: Cidade, custo_do_caminho: int):
        self.cidade_destino = cidade_destino
        self.custo_do_caminho = custo_do_caminho

    @property
    def destino(self):
        return self.cidade_destino

    @property
    def custo(self):
        return self.custo_do_caminho
