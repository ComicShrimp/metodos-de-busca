from typing import List

from metodos_de_busca.sociedade import Cidade

from .busca import IBusca, BuscaInputDto, ResultadoBusca


class BuscaAEstrela(IBusca):  # A*
    def __init__(self):
        self.arvore_de_cidades: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        raise Exception("Não implementado")
