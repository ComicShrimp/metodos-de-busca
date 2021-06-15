from typing import List
from src.cidade import Cidade, adjascente


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
        self.arad.adjascentes = [self.zerind, self.sibiu, self.timisoara]
        self.bucharest.adjascentes = [
            self.giurgiu,
            self.urziceni,
            self.fagaras,
            self.pitesti,
        ]
        self.craiova.adjascentes = [self.pitesti, self.rimnicu_vilcea, self.dobreta]
        self.dobreta.adjascentes = [self.craiova, self.mehadia]
        self.eforie.adjascentes = [self.hirsova]
        self.fagaras.adjascentes = [self.sibiu, self.bucharest]
        self.giurgiu.adjascentes = [self.bucharest]
        self.hirsova.adjascentes = [self.eforie, self.urziceni]
        self.iasi.adjascentes = [self.neamt, self.vaslui]
        self.lugoj.adjascentes = [self.mehadia, self.timisoara]
        self.mehadia.adjascentes = [self.lugoj, self.dobreta]
        self.neamt.adjascentes = [self.iasi]
        self.oradea.adjascentes = [self.zerind, self.sibiu]
        self.pitesti.adjascentes = [self.rimnicu_vilcea, self.craiova, self.bucharest]
        self.rimnicu_vilcea.adjascentes = [self.pitesti, self.craiova, self.sibiu]
        self.sibiu.adjascentes = [
            self.fagaras,
            self.arad,
            self.oradea,
            self.rimnicu_vilcea,
        ]
        self.timisoara.adjascentes = [self.lugoj, self.arad]
        self.urziceni.adjascentes = [self.hirsova, self.bucharest]
        self.vaslui.adjascentes = [self.iasi, self.urziceni]
        self.zerind.adjascentes = [self.oradea, self.arad]

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
