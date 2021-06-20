from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union

from metodos_de_busca.cidade import Cidade

from .resultado import ResultadoBusca


@dataclass
class BuscaInputDto:
    partida: Cidade
    chegada: Cidade


class IBusca(ABC):
    @abstractmethod
    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        pass
