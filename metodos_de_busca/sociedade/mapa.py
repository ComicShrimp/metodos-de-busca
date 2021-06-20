from typing import List
from metodos_de_busca.sociedade.cidade import Cidade, Adjascente


class Mapa:
    def __init__(self) -> None:
        # TODO: ler arquivo json para montar o mapa
        self.arad = Cidade("Arad", 366)
        self.bucharest = Cidade("Bucharest", 0)
        self.craiova = Cidade("Craiova", 160)
        self.dobreta = Cidade("Dobreta", 242)
        self.eforie = Cidade("Eforie", 161)
        self.fagaras = Cidade("Fagaras", 178)
        self.giurgiu = Cidade("Giurgiu", 77)
        self.hirsova = Cidade("Hirsova", 151)
        self.iasi = Cidade("Iasi", 226)
        self.lugoj = Cidade("Lugoj", 244)
        self.mehadia = Cidade("Mehadia", 241)
        self.neamt = Cidade("Neamt", 234)
        self.oradea = Cidade("Oradea", 380)
        self.pitesti = Cidade("pitesti", 98)
        self.rimnicu_vilcea = Cidade("Rimnicu Vilcea", 193)
        self.sibiu = Cidade("Sibiu", 253)
        self.timisoara = Cidade("Timisoara", 329)
        self.urziceni = Cidade("Urziceni", 80)
        self.vaslui = Cidade("Vaslui", 199)
        self.zerind = Cidade("Zerind", 374)

        self.cidades: List[Cidade] = []
        self.pilha: List[Cidade] = []

        self._cria_cidades_adjacentes()
        self._cria_mapa()

    @property
    def partida(self):
        return self.cidades[0]

    @property
    def chegada(self):
        return self.cidades[1]

    def get_mapa(self):
        return self.cidades

    def _limpa_busca(self):
        for cidade in self.cidades:
            cidade.reiniciar_visitado()

        self.pilha = []

    def _cria_cidades_adjacentes(self):
        self.arad.adjascentes = [
            Adjascente(self.zerind, 75),
            Adjascente(self.sibiu, 140),
            Adjascente(self.timisoara, 118),
        ]
        self.bucharest.adjascentes = [
            Adjascente(self.giurgiu, 90),
            Adjascente(self.urziceni, 85),
            Adjascente(self.fagaras, 211),
            Adjascente(self.pitesti, 101),
        ]
        self.craiova.adjascentes = [
            Adjascente(self.pitesti, 138),
            Adjascente(self.rimnicu_vilcea, 146),
            Adjascente(self.dobreta, 120),
        ]
        self.dobreta.adjascentes = [
            Adjascente(self.craiova, 120),
            Adjascente(self.mehadia, 75),
        ]
        self.eforie.adjascentes = [Adjascente(self.hirsova, 86)]
        self.fagaras.adjascentes = [
            Adjascente(self.sibiu, 99),
            Adjascente(self.bucharest, 211),
        ]
        self.giurgiu.adjascentes = [Adjascente(self.bucharest, 90)]
        self.hirsova.adjascentes = [
            Adjascente(self.eforie, 86),
            Adjascente(self.urziceni, 98),
        ]
        self.iasi.adjascentes = [
            Adjascente(self.neamt, 87),
            Adjascente(self.vaslui, 92),
        ]
        self.lugoj.adjascentes = [
            Adjascente(self.mehadia, 70),
            Adjascente(self.timisoara, 111),
        ]
        self.mehadia.adjascentes = [
            Adjascente(self.lugoj, 70),
            Adjascente(self.dobreta, 75),
        ]
        self.neamt.adjascentes = [Adjascente(self.iasi, 87)]
        self.oradea.adjascentes = [
            Adjascente(self.zerind, 71),
            Adjascente(self.sibiu, 151),
        ]
        self.pitesti.adjascentes = [
            Adjascente(self.rimnicu_vilcea, 97),
            Adjascente(self.craiova, 138),
            Adjascente(self.bucharest, 101),
        ]
        self.rimnicu_vilcea.adjascentes = [
            Adjascente(self.pitesti, 97),
            Adjascente(self.craiova, 146),
            Adjascente(self.sibiu, 80),
        ]
        self.sibiu.adjascentes = [
            Adjascente(self.fagaras, 99),
            Adjascente(self.arad, 140),
            Adjascente(self.oradea, 151),
            Adjascente(self.rimnicu_vilcea, 80),
        ]
        self.timisoara.adjascentes = [
            Adjascente(self.lugoj, 111),
            Adjascente(self.arad, 118),
        ]
        self.urziceni.adjascentes = [
            Adjascente(self.hirsova, 98),
            Adjascente(self.bucharest, 85),
        ]
        self.vaslui.adjascentes = [
            Adjascente(self.iasi, 92),
            Adjascente(self.urziceni, 142),
        ]
        self.zerind.adjascentes = [
            Adjascente(self.oradea, 71),
            Adjascente(self.arad, 75),
        ]

    def _cria_mapa(self):
        self.cidades.append(
            self.arad,
        )
        self.cidades.append(
            self.bucharest,
        )
        self.cidades.append(
            self.craiova,
        )
        self.cidades.append(
            self.dobreta,
        )
        self.cidades.append(
            self.eforie,
        )
        self.cidades.append(
            self.fagaras,
        )
        self.cidades.append(
            self.giurgiu,
        )
        self.cidades.append(
            self.hirsova,
        )
        self.cidades.append(
            self.iasi,
        )
        self.cidades.append(
            self.lugoj,
        )
        self.cidades.append(
            self.mehadia,
        )
        self.cidades.append(
            self.neamt,
        )
        self.cidades.append(
            self.oradea,
        )
        self.cidades.append(
            self.pitesti,
        )
        self.cidades.append(
            self.rimnicu_vilcea,
        )
        self.cidades.append(
            self.sibiu,
        )
        self.cidades.append(
            self.timisoara,
        )
        self.cidades.append(
            self.urziceni,
        )
        self.cidades.append(
            self.vaslui,
        )
        self.cidades.append(
            self.zerind,
        )
