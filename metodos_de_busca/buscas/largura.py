from typing import List

from metodos_de_busca.sociedade import Cidade, Vizinho

from .busca import IBusca, BuscaInputDto, ResultadoBusca


class BuscaEmLargura(IBusca):
    def __init__(self):
        self.arvore_de_cidades: List[Cidade] = []
        self.caminho_final: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        fila: List[Cidade] = []
        fila.append(input_dto.partida)

        while fila:
            nova_fila: List[Cidade] = []

            for cidade in fila:
                if not cidade.foi_visitado():
                    cidade.visitar()
                    self.arvore_de_cidades.append(cidade)
                    if cidade.eh_igual(input_dto.chegada):
                        return ResultadoBusca(arvore_de_cidades=self.arvore_de_cidades)
                    else:
                        for vizinho in cidade.vizinhos:
                            nova_fila.append(vizinho.destino)

            fila = nova_fila

        return ResultadoBusca(caminho_nao_encontrado=True)
