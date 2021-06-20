from typing import List, Union

from metodos_de_busca.cidade import Cidade

from .busca import IBusca, BuscaInputDto
from .resultado import ResultadoBusca


class BuscaProfunda(IBusca):
    def __init__(self):
        self.arvore_de_busca: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> Union[ResultadoBusca, bool]:
        input_dto.partida.visitar()

        self.arvore_de_busca.append(input_dto.partida)

        if input_dto.partida.nome == input_dto.chegada.nome:
            return ResultadoBusca(self.arvore_de_busca)
        else:
            for adjascente in input_dto.partida.adjascentes:
                if not adjascente.cidade_destino.foi_visitado():
                    print("Busca: " + adjascente.cidade_destino.nome)
                    resultado = self.executa(
                        BuscaInputDto(
                            partida=adjascente.cidade_destino,
                            chegada=input_dto.chegada,
                        )
                    )
                    if resultado:
                        return ResultadoBusca(self.arvore_de_busca)
                    self.arvore_de_busca.pop()
        return False
