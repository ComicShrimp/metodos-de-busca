from typing import List
from src.cidade import Cidade, Adjascente


class Mapa:
    arad = Cidade("Arad", 366)
    bucharest = Cidade("Bucharest", 0)
    craiova = Cidade("Craiova", 160)
    dobreta = Cidade("Dobreta", 242)
    eforie = Cidade("Eforie", 161)
    fagaras = Cidade("Fagaras", 178)
    giurgiu = Cidade("Giurgiu", 77)
    hirsova = Cidade("Hirsova", 151)
    iasi = Cidade("Iasi", 226)
    lugoj = Cidade("Lugoj", 244)
    mehadia = Cidade("Mehadia", 241)
    neamt = Cidade("Neamt", 234)
    oradea = Cidade("Oradea", 380)
    pitesti = Cidade("pitesti", 98)
    rimnicu_vilcea = Cidade("Rimnicu Vilcea", 193)
    sibiu = Cidade("Sibiu", 253)
    timisoara = Cidade("Timisoara", 329)
    urziceni = Cidade("Urziceni", 80)
    vaslui = Cidade("Vaslui", 199)
    zerind = Cidade("Zerind", 374)

    cidades: List[Cidade] = []
    pilha: List[Cidade] = []

    def __init__(self) -> None:
        self._cria_cidades_adjacentes()
        self._cria_mapa()

    def busca_profunda(self, partida: Cidade, chegada: Cidade):
        partida.visitado = True
        self.pilha.append(partida)

        if partida.nome == chegada.nome:
            return self.pilha
        else:
            for cidade in partida.adjascentes:
                if not cidade.visitado:
                    print("Busca: " + cidade.nome)
                    resultado = self.busca_profunda(cidade, chegada)
                    if resultado:
                        return self.pilha
                    self.pilha.pop()
        return False

    def busca_largura(self, partida: str, chegada: str) -> List[str]:
        return [partida, chegada]

    def busca_a_estrela(self, partida: str, chegada: str) -> List[str]:
        return [partida, chegada]

    def busca_gulosa(self, partida: str, chegada: str) -> List[str]:
        return [partida, chegada]

    def busca_custo_uniforme(self, partida: str, chegada: str) -> List[str]:
        return [partida, chegada]

    def _limpa_busca(self):
        for cidade in self.cidades:
            cidade.cidade.visitado = False

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
