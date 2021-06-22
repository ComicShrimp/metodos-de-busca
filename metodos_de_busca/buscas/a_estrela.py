from typing import List, Optional

from metodos_de_busca.sociedade import Cidade

from .busca import (
    IBusca,
    BuscaInputDto,
    ResultadoBusca,
)


class BuscaAEstrela(IBusca):  # A*
    def __init__(self):
        self.arvore_de_cidades: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        pass
        # cidade_atual = input_dto.partida

        # while cidade_atual is not None:
        #     if cidade_atual.eh_igual(input_dto.chegada):
        #         return ResultadoBusca(arvore_de_cidades=self.arvore_de_cidades)

        #     for vizinho in cidade_atual.vizinhos:
        #         if vizinho.destino.eh_igual(input_dto.chegada):
        #             return ResultadoBusca(arvore_de_cidades=self.arvore_de_cidades)

        #         if input_dto.heuristica is not None:
        #             heuristica = acha_distancia_heuristica(
        #                 vizinho.destino, input_dto.heuristica
        #             )
        #             if heuristica is not None:
        #                 g_e_f = heuristica.distancia + vizinho.custo

        #     cidade_atual = None
        # raise Exception("parei aqui")
        # return ResultadoBusca(caminho_nao_encontrado=True)
