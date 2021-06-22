from metodos_de_busca.sociedade.cidade import Vizinho
from typing import List

from metodos_de_busca.sociedade import Cidade

from .busca import IBusca, BuscaInputDto, ResultadoBusca


class BuscaGulosa(IBusca):
    def __init__(self):
        self.arvore_de_busca: List[Vizinho] = []
        self.caminho: List[Vizinho] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        input_dto.partida.visitar()

        if input_dto.partida.nome == input_dto.chegada.nome:
            return ResultadoBusca(
                caminho=self.caminho, arvore_de_cidades=self.arvore_de_busca
            )
        else:
            if input_dto.partida.vizinhos[0].cidade_destino.foi_visitado():
                cidade_a_visitar = input_dto.partida.vizinhos[1]
            else:
                cidade_a_visitar = input_dto.partida.vizinhos[0]

            for vizinho in input_dto.partida.vizinhos:
                if not vizinho.cidade_destino.foi_visitado():
                    custo = vizinho.cidade_destino.heuristica
                    custo_a_visitar = cidade_a_visitar.cidade_destino.heuristica
                    if custo < custo_a_visitar:
                        cidade_a_visitar = vizinho

            self.arvore_de_busca.append(cidade_a_visitar)
            self.caminho.append(cidade_a_visitar)

            return self.executa(
                BuscaInputDto(
                    partida=cidade_a_visitar.cidade_destino,
                    chegada=input_dto.chegada,
                )
            )
