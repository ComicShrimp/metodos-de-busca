from typing import List
from cidade_mapa import CidadeMapa
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
    cidades: List[CidadeMapa] = []

    def __init__(self) -> None:
        self.cidades.append(
            CidadeMapa(self.arad, [self.zerind, self.sibiu, self.timisoara])
        )
        self.cidades.append(
            CidadeMapa(
                self.bucharest,
                [self.giurgiu, self.urziceni, self.fagaras, self.pitesti],
            )
        )
        self.cidades.append(
            CidadeMapa(self.craiova, [self.pitesti, self.rimnicu_vilcea, self.dobreta])
        )
        self.cidades.append(CidadeMapa(self.dobreta, [self.craiova, self.mehadia]))
        self.cidades.append(CidadeMapa(self.eforie, [self.hirsova]))
        self.cidades.append(CidadeMapa(self.fagaras, [self.sibiu, self.bucharest]))
        self.cidades.append(CidadeMapa(self.giurgiu, [self.bucharest]))
        self.cidades.append(CidadeMapa(self.hirsova, [self.eforie, self.urziceni]))
        self.cidades.append(CidadeMapa(self.iasi, [self.neamt, self.vaslui]))
        self.cidades.append(CidadeMapa(self.lugoj, [self.mehadia, self.timisoara]))
        self.cidades.append(CidadeMapa(self.mehadia, [self.lugoj, self.dobreta]))
        self.cidades.append(CidadeMapa(self.neamt, [self.iasi]))
        self.cidades.append(CidadeMapa(self.oradea, [self.zerind, self.sibiu]))
        self.cidades.append(
            CidadeMapa(
                self.pitesti, [self.rimnicu_vilcea, self.craiova, self.bucharest]
            )
        )
        self.cidades.append(
            CidadeMapa(self.rimnicu_vilcea, [self.pitesti, self.craiova, self.sibiu])
        )
        self.cidades.append(
            CidadeMapa(
                self.sibiu, [self.fagaras, self.arad, self.oradea, self.rimnicu_vilcea]
            )
        )
        self.cidades.append(CidadeMapa(self.timisoara, [self.lugoj, self.arad]))
        self.cidades.append(CidadeMapa(self.urziceni, [self.hirsova, self.bucharest]))
        self.cidades.append(CidadeMapa(self.vaslui, [self.iasi, self.urziceni]))
        self.cidades.append(CidadeMapa(self.zerind, [self.oradea, self.arad]))

    def busca_profunda(partida: CidadeMapa, chegada: CidadeMapa) -> List[CidadeMapa]:
        return [partida, chegada]

    def busca_largura(partida: CidadeMapa, chegada: CidadeMapa) -> List[CidadeMapa]:
        return [partida, chegada]

    def busca_a_estrela(partida: CidadeMapa, chegada: CidadeMapa) -> List[CidadeMapa]:
        return [partida, chegada]

    def busca_gulosa(partida: CidadeMapa, chegada: CidadeMapa) -> List[CidadeMapa]:
        return [partida, chegada]

    def busca_custo_uniforme(
        partida: CidadeMapa, chegada: CidadeMapa
    ) -> List[CidadeMapa]:
        return [partida, chegada]

    def _limpa_busca(self):
        for cidade in self.cidades:
            cidade.cidade.visitado = False
