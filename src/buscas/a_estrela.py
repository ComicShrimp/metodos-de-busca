from typing import List, Union

from cidade import Cidade

from .busca import IBusca, BuscaInputDto
from .resultado import ResultadoBusca


class BucasAEstrela(IBusca):  # A*
    def __init__(self):
        self.pilha: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> Union[ResultadoBusca, bool]:
        # TODO: implementar
        pass
