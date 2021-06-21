from typing import List
from metodos_de_busca.buscas.busca import DistanciaEmLinhaRetaParaDestino

from metodos_de_busca.sociedade.cidade import Cidade, Vizinho


class Mapa:
    def __init__(self) -> None:
        # TODO: ler arquivo json para montar o mapa
        self.arad = Cidade("Arad")
        self.bucharest = Cidade("Bucharest")
        self.craiova = Cidade("Craiova")
        self.dobreta = Cidade("Dobreta")
        self.eforie = Cidade("Eforie")
        self.fagaras = Cidade("Fagaras")
        self.giurgiu = Cidade("Giurgiu")
        self.hirsova = Cidade("Hirsova")
        self.iasi = Cidade("Iasi")
        self.lugoj = Cidade("Lugoj")
        self.mehadia = Cidade("Mehadia")
        self.neamt = Cidade("Neamt")
        self.oradea = Cidade("Oradea")
        self.pitesti = Cidade("pitesti")
        self.rimnicu_vilcea = Cidade("Rimnicu Vilcea")
        self.sibiu = Cidade("Sibiu")
        self.timisoara = Cidade("Timisoara")
        self.urziceni = Cidade("Urziceni")
        self.vaslui = Cidade("Vaslui")
        self.zerind = Cidade("Zerind")

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

    def get_heuristica(self):
        return [
            DistanciaEmLinhaRetaParaDestino(cidade=self.arad, distancia=366),
            DistanciaEmLinhaRetaParaDestino(cidade=self.bucharest, distancia=0),
            DistanciaEmLinhaRetaParaDestino(cidade=self.craiova, distancia=160),
            DistanciaEmLinhaRetaParaDestino(cidade=self.dobreta, distancia=242),
            DistanciaEmLinhaRetaParaDestino(cidade=self.eforie, distancia=161),
            DistanciaEmLinhaRetaParaDestino(cidade=self.fagaras, distancia=178),
            DistanciaEmLinhaRetaParaDestino(cidade=self.bucharest, distancia=0),
            DistanciaEmLinhaRetaParaDestino(cidade=self.giurgiu, distancia=77),
            DistanciaEmLinhaRetaParaDestino(cidade=self.hirsova, distancia=151),
            DistanciaEmLinhaRetaParaDestino(cidade=self.iasi, distancia=226),
            DistanciaEmLinhaRetaParaDestino(cidade=self.lugoj, distancia=244),
            DistanciaEmLinhaRetaParaDestino(cidade=self.mehadia, distancia=241),
            DistanciaEmLinhaRetaParaDestino(cidade=self.neamt, distancia=234),
            DistanciaEmLinhaRetaParaDestino(cidade=self.oradea, distancia=380),
            DistanciaEmLinhaRetaParaDestino(cidade=self.pitesti, distancia=98),
            DistanciaEmLinhaRetaParaDestino(cidade=self.rimnicu_vilcea, distancia=193),
            DistanciaEmLinhaRetaParaDestino(cidade=self.sibiu, distancia=253),
            DistanciaEmLinhaRetaParaDestino(cidade=self.timisoara, distancia=329),
            DistanciaEmLinhaRetaParaDestino(cidade=self.urziceni, distancia=80),
            DistanciaEmLinhaRetaParaDestino(cidade=self.vaslui, distancia=199),
            DistanciaEmLinhaRetaParaDestino(cidade=self.zerind, distancia=374),
        ]

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
