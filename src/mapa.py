from typing import List
from cidades import Cidades


class Mapa:
    cidades: List = [
        {
            "nome": Cidades.arad,
            "adjascente": [Cidades.zerind, Cidades.sibiu, Cidades.timisoara],
            "visitado": False,
        },
        {
            "nome": Cidades.bucharest,
            "adjascente": [
                Cidades.giurgiu,
                Cidades.urziceni,
                Cidades.fagaras,
                Cidades.pitesti,
            ],
            "visitado": False,
        },
        {
            "nome": Cidades.craiova,
            "adjascente": [Cidades.pitesti, Cidades.rimnicu_vilcea, Cidades.dobreta],
            "visitado": False,
        },
        {
            "nome": Cidades.dobreta,
            "adjascente": [Cidades.craiova, Cidades.mehadia],
            "visitado": False,
        },
        {"nome": Cidades.eforie, "adjascente": [Cidades.hirsova], "visitado": False},
        {
            "nome": Cidades.fagaras,
            "adjascente": [Cidades.sibiu, Cidades.bucharest],
            "visitado": False,
        },
        {"nome": Cidades.giurgiu, "adjascente": [Cidades.bucharest], "visitado": False},
        {
            "nome": Cidades.hirsova,
            "adjascente": [Cidades.eforie, Cidades.urziceni],
            "visitado": False,
        },
        {
            "nome": Cidades.iasi,
            "adjascente": [Cidades.neamt, Cidades.vaslui],
            "visitado": False,
        },
        {
            "nome": Cidades.lugoj,
            "adjascente": [Cidades.mehadia, Cidades.timisoara],
            "visitado": False,
        },
        {
            "nome": Cidades.mehadia,
            "adjascente": [Cidades.lugoj, Cidades.dobreta],
            "visitado": False,
        },
        {"nome": Cidades.neamt, "adjascente": [Cidades.iasi], "visitado": False},
        {
            "nome": Cidades.oradea,
            "adjascente": [Cidades.zerind, Cidades.sibiu],
            "visitado": False,
        },
        {
            "nome": Cidades.pitesti,
            "adjascente": [Cidades.rimnicu_vilcea, Cidades.craiova, Cidades.bucharest],
            "visitado": False,
        },
        {
            "nome": Cidades.rimnicu_vilcea,
            "adjascente": [Cidades.pitesti, Cidades.craiova, Cidades.sibiu],
            "visitado": False,
        },
        {
            "nome": Cidades.sibiu,
            "adjascente": [
                Cidades.fagaras,
                Cidades.arad,
                Cidades.oradea,
                Cidades.rimnicu_vilcea,
            ],
            "visitado": False,
        },
        {
            "nome": Cidades.timisoara,
            "adjascente": [Cidades.lugoj, Cidades.arad],
            "visitado": False,
        },
        {
            "nome": Cidades.urziceni,
            "adjascente": [Cidades.hirsova, Cidades.bucharest],
            "visitado": False,
        },
        {
            "nome": Cidades.vaslui,
            "adjascente": [Cidades.iasi, Cidades.urziceni],
            "visitado": False,
        },
        {
            "nome": Cidades.zerind,
            "adjascente": [Cidades.oradea, Cidades.arad],
            "visitado": False,
        },
    ]

    def busca_profunda(self, partida: str, chegada: str) -> List[str]:
        print(partida)
        return [partida]
        # retorno = [partida.nome]
        # if partida.nome == chegada.nome:
        #     return retorno
        # else:
        #     return partida + self.busca_profunda(
        #         partida.cidades_adjascentes[0], chegada
        #     )

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
