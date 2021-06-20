from typing import List

from metodos_de_busca.sociedade import Cidade

from .busca import IBusca, BuscaInputDto
from .resultado import ResultadoBusca


class BucasEmLargura(IBusca):
    def __init__(self):
        self.pilha: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        # TODO: implementar
        pass
