from typing import List
from cidade_mapa import CidadeMapa
from cidade import Cidade


class Mapa:
    cidades: List[CidadeMapa] = []

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

    def cria_mapa(self) -> List[CidadeMapa]:
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

        self.cidades.append(CidadeMapa(arad, [zerind, sibiu, timisoara]))
        self.cidades.append(
            CidadeMapa(bucharest, [giurgiu, urziceni, fagaras, pitesti])
        )
        self.cidades.append(CidadeMapa(craiova, [pitesti, rimnicu_vilcea, dobreta]))
        self.cidades.append(CidadeMapa(dobreta, [craiova, mehadia]))
        self.cidades.append(CidadeMapa(eforie, [hirsova]))
        self.cidades.append(CidadeMapa(fagaras, [sibiu, bucharest]))
        self.cidades.append(CidadeMapa(giurgiu, [bucharest]))
        self.cidades.append(CidadeMapa(hirsova, [eforie, urziceni]))
        self.cidades.append(CidadeMapa(iasi, [neamt, vaslui]))
        self.cidades.append(CidadeMapa(lugoj, [mehadia, timisoara]))
        self.cidades.append(CidadeMapa(mehadia, [lugoj, dobreta]))
        self.cidades.append(CidadeMapa(neamt, [iasi]))
        self.cidades.append(CidadeMapa(oradea, [zerind, sibiu]))
        self.cidades.append(CidadeMapa(pitesti, [rimnicu_vilcea, craiova, bucharest]))
        self.cidades.append(CidadeMapa(rimnicu_vilcea, [pitesti, craiova, sibiu]))
        self.cidades.append(CidadeMapa(sibiu, [fagaras, arad, oradea, rimnicu_vilcea]))
        self.cidades.append(CidadeMapa(timisoara, [lugoj, arad]))
        self.cidades.append(CidadeMapa(urziceni, [hirsova, bucharest]))
        self.cidades.append(CidadeMapa(vaslui, [iasi, urziceni]))
        self.cidades.append(CidadeMapa(zerind, [oradea, arad]))

        return self.cidades

    def _limpa_busca(self):
        for cidade in self.cidades:
            cidade.cidade.visitado = False
