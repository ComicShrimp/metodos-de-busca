from abc import ABC, abstractmethod
from dataclasses import dataclass

from metodos_de_busca.sociedade import Cidade

from dataclasses import dataclass
from typing import List, Optional

from metodos_de_busca.sociedade import Cidade


@dataclass
class BuscaInputDto:
    partida: Cidade
    chegada: Cidade


@dataclass
class ResultadoBusca:
    arvore_de_cidades: Optional[List[Cidade]] = None
    caminho_impossivel: bool = False


class IBusca(ABC):
    @abstractmethod
    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        pass
