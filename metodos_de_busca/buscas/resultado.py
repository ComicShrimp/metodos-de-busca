from dataclasses import dataclass
from typing import List

from metodos_de_busca.cidade import Cidade


@dataclass
class ResultadoBusca:
    arvore_de_cidades: List[Cidade]
