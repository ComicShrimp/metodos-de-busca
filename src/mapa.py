from typing import List
from cidade import Cidade


class Mapa:
    arad = Cidade("Arad")
    bucharest = Cidade("Bucharest")
    craiova = Cidade("Craiova")
    dobreta = Cidade("Dobreta")
    eforie = Cidade("Eforie")
    fagaras = Cidade("Fagaras")
    giurgiu = Cidade("Giurgiu")
    hirsova = Cidade("Hirsova")
    iasi = Cidade("Iasi")
    lugoj = Cidade("Lugoj")
    mehadia = Cidade("Mehadia")
    neamt = Cidade("Neamt")
    oradea = Cidade("Oradea")
    pitesti = Cidade("pitesti")
    rimnicu_vilcea = Cidade("Rimnicu Vilcea")
    sibiu = Cidade("Sibiu")
    timisoara = Cidade("Timisoara")
    urziceni = Cidade("Urziceni")
    vaslui = Cidade("Vaslui")
    zerind = Cidade("Zerind")
    cidades: List[Cidade] = []

    def __init__(self) -> None:
        self.cidades.append(
            Cidade(self.arad, [self.zerind, self.sibiu, self.timisoara])
        )
        self.cidades.append(
            Cidade(
                self.bucharest,
                [self.giurgiu, self.urziceni, self.fagaras, self.pitesti],
            )
        )
        self.cidades.append(
            Cidade(self.craiova, [self.pitesti, self.rimnicu_vilcea, self.dobreta])
        )
        self.cidades.append(Cidade(self.dobreta, [self.craiova, self.mehadia]))
        self.cidades.append(Cidade(self.eforie, [self.hirsova]))
        self.cidades.append(Cidade(self.fagaras, [self.sibiu, self.bucharest]))
        self.cidades.append(Cidade(self.giurgiu, [self.bucharest]))
        self.cidades.append(Cidade(self.hirsova, [self.eforie, self.urziceni]))
        self.cidades.append(Cidade(self.iasi, [self.neamt, self.vaslui]))
        self.cidades.append(Cidade(self.lugoj, [self.mehadia, self.timisoara]))
        self.cidades.append(Cidade(self.mehadia, [self.lugoj, self.dobreta]))
        self.cidades.append(Cidade(self.neamt, [self.iasi]))
        self.cidades.append(Cidade(self.oradea, [self.zerind, self.sibiu]))
        self.cidades.append(
            Cidade(self.pitesti, [self.rimnicu_vilcea, self.craiova, self.bucharest])
        )
        self.cidades.append(
            Cidade(self.rimnicu_vilcea, [self.pitesti, self.craiova, self.sibiu])
        )
        self.cidades.append(
            Cidade(
                self.sibiu, [self.fagaras, self.arad, self.oradea, self.rimnicu_vilcea]
            )
        )
        self.cidades.append(Cidade(self.timisoara, [self.lugoj, self.arad]))
        self.cidades.append(Cidade(self.urziceni, [self.hirsova, self.bucharest]))
        self.cidades.append(Cidade(self.vaslui, [self.iasi, self.urziceni]))
        self.cidades.append(Cidade(self.zerind, [self.oradea, self.arad]))

    def busca_profunda(partida: Cidade, chegada: Cidade) -> List[Cidade]:
        return [partida, chegada]

    def busca_largura(partida: Cidade, chegada: Cidade) -> List[Cidade]:
        return [partida, chegada]

    def busca_a_estrela(partida: Cidade, chegada: Cidade) -> List[Cidade]:
        return [partida, chegada]

    def busca_gulosa(partida: Cidade, chegada: Cidade) -> List[Cidade]:
        return [partida, chegada]

    def busca_custo_uniforme(partida: Cidade, chegada: Cidade) -> List[Cidade]:
        return [partida, chegada]

    def _limpa_busca(self):
        for cidade in self.cidades:
            cidade.cidade.visitado = False
