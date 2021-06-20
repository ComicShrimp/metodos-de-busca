from typing import List
from metodos_de_busca.sociedade.cidade import Cidade, Vizinho


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
        self.arad.vizinhos = [
            Vizinho(self.zerind, 75),
            Vizinho(self.sibiu, 140),
            Vizinho(self.timisoara, 118),
        ]
        self.bucharest.vizinhos = [
            Vizinho(self.giurgiu, 90),
            Vizinho(self.urziceni, 85),
            Vizinho(self.fagaras, 211),
            Vizinho(self.pitesti, 101),
        ]
        self.craiova.vizinhos = [
            Vizinho(self.pitesti, 138),
            Vizinho(self.rimnicu_vilcea, 146),
            Vizinho(self.dobreta, 120),
        ]
        self.dobreta.vizinhos = [
            Vizinho(self.craiova, 120),
            Vizinho(self.mehadia, 75),
        ]
        self.eforie.vizinhos = [Vizinho(self.hirsova, 86)]
        self.fagaras.vizinhos = [
            Vizinho(self.sibiu, 99),
            Vizinho(self.bucharest, 211),
        ]
        self.giurgiu.vizinhos = [Vizinho(self.bucharest, 90)]
        self.hirsova.vizinhos = [
            Vizinho(self.eforie, 86),
            Vizinho(self.urziceni, 98),
        ]
        self.iasi.vizinhos = [
            Vizinho(self.neamt, 87),
            Vizinho(self.vaslui, 92),
        ]
        self.lugoj.vizinhos = [
            Vizinho(self.mehadia, 70),
            Vizinho(self.timisoara, 111),
        ]
        self.mehadia.vizinhos = [
            Vizinho(self.lugoj, 70),
            Vizinho(self.dobreta, 75),
        ]
        self.neamt.vizinhos = [Vizinho(self.iasi, 87)]
        self.oradea.vizinhos = [
            Vizinho(self.zerind, 71),
            Vizinho(self.sibiu, 151),
        ]
        self.pitesti.vizinhos = [
            Vizinho(self.rimnicu_vilcea, 97),
            Vizinho(self.craiova, 138),
            Vizinho(self.bucharest, 101),
        ]
        self.rimnicu_vilcea.vizinhos = [
            Vizinho(self.pitesti, 97),
            Vizinho(self.craiova, 146),
            Vizinho(self.sibiu, 80),
        ]
        self.sibiu.vizinhos = [
            Vizinho(self.fagaras, 99),
            Vizinho(self.arad, 140),
            Vizinho(self.oradea, 151),
            Vizinho(self.rimnicu_vilcea, 80),
        ]
        self.timisoara.vizinhos = [
            Vizinho(self.lugoj, 111),
            Vizinho(self.arad, 118),
        ]
        self.urziceni.vizinhos = [
            Vizinho(self.hirsova, 98),
            Vizinho(self.bucharest, 85),
        ]
        self.vaslui.vizinhos = [
            Vizinho(self.iasi, 92),
            Vizinho(self.urziceni, 142),
        ]
        self.zerind.vizinhos = [
            Vizinho(self.oradea, 71),
            Vizinho(self.arad, 75),
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
