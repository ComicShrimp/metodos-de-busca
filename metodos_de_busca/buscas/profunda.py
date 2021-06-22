from typing import List

from metodos_de_busca.sociedade import Cidade

from .busca import IBusca, BuscaInputDto, ResultadoBusca


class BuscaProfunda(IBusca):
    def __init__(self):
        self.arvore_de_busca: List[Cidade] = []
        self.caminho: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        input_dto.partida.visitar()

        self.caminho.append(input_dto.partida)

        if input_dto.partida.nome == input_dto.chegada.nome:
            return ResultadoBusca(
                caminho=self.caminho, arvore_de_cidades=self.arvore_de_busca
            )
        else:
            for vizinho in input_dto.partida.vizinhos:
                if not vizinho.cidade_destino.foi_visitado():
                    self.arvore_de_busca.append(vizinho)

                    resultado = self.executa(
                        BuscaInputDto(
                            partida=vizinho.cidade_destino,
                            chegada=input_dto.chegada,
                        )
                    )
                    if resultado:
                        return ResultadoBusca(
                            caminho=self.caminho, arvore_de_cidades=self.arvore_de_busca
                        )
                    self.caminho.pop()

        return ResultadoBusca(caminho_nao_encontrado=True)
