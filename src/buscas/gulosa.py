from typing import List, Union

from cidade import Cidade

from .busca import IBusca, BuscaInputDto
from .resultado import ResultadoBusca


class BuscaGulosa(IBusca):
    def __init__(self):
        self.arvore_de_busca: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> Union[ResultadoBusca, bool]:
        input_dto.partida.visitar()

        self.arvore_de_busca.append(input_dto.partida)

        if input_dto.partida.nome == input_dto.chegada.nome:
            return ResultadoBusca(self.arvore_de_busca)
        else:
            if input_dto.partida.adjascentes[0].cidade_destino.foi_visitado():
                cidade_a_visitar = input_dto.partida.adjascentes[1]
            else:
                cidade_a_visitar = input_dto.partida.adjascentes[0]

            for adjascente in input_dto.partida.adjascentes:
                if not adjascente.cidade_destino.foi_visitado():
                    custo = adjascente.custo_do_caminho
                    custo_a_visitar = cidade_a_visitar.custo_do_caminho
                    if custo < custo_a_visitar:
                        cidade_a_visitar = adjascente

            print("Busca: " + cidade_a_visitar.cidade_destino.nome)
            return self.executa(
                BuscaInputDto(
                    partida=cidade_a_visitar.cidade_destino,
                    chegada=input_dto.chegada,
                )
            )
