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
    caminho_nao_encontrado: bool = False

    def exporta(self):
        resultado = []

        if self.arvore_de_cidades is not None:
            for cidade in self.arvore_de_cidades:
                resultado.append(f"Cidade: {cidade.nome}, Custo: { cidade.custo}")

        return resultado


class IBusca(ABC):
    @abstractmethod
    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        pass
