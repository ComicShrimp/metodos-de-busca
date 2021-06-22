from typing import List, Optional

from metodos_de_busca.sociedade import Cidade

from .busca import (
    IBusca,
    BuscaInputDto,
    ResultadoBusca,
)


class BuscaAEstrela(IBusca):  # A*
    def __init__(self):
        self.arvore_de_busca: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        input_dto.partida.visitar()

        self.arvore_de_busca.append(input_dto.partida)

        if input_dto.partida.nome == input_dto.chegada.nome:
            return ResultadoBusca(self.arvore_de_busca)
        else:
            if input_dto.partida.vizinhos[0].cidade_destino.foi_visitado():
                cidade_a_visitar = input_dto.partida.vizinhos[1]
            else:
                cidade_a_visitar = input_dto.partida.vizinhos[0]

            for vizinho in input_dto.partida.vizinhos:
                if not vizinho.cidade_destino.foi_visitado():
                    custo = vizinho.cidade_destino.heuristica + vizinho.custo_do_caminho
                    custo_a_visitar = (
                        cidade_a_visitar.cidade_destino.heuristica
                        + cidade_a_visitar.custo_do_caminho
                    )
                    if custo < custo_a_visitar:
                        cidade_a_visitar = vizinho

            print("Busca: " + cidade_a_visitar.cidade_destino.nome)
            return self.executa(
                BuscaInputDto(
                    partida=cidade_a_visitar.cidade_destino,
                    chegada=input_dto.chegada,
                )
            )
