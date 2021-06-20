from abc import ABC, abstractmethod
from dataclasses import dataclass

from metodos_de_busca.sociedade import Cidade

from .resultado import ResultadoBusca


@dataclass
class BuscaInputDto:
    partida: Cidade
    chegada: Cidade


class IBusca(ABC):
    @abstractmethod
    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        pass
