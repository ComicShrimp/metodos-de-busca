from dataclasses import dataclass
from typing import List

from cidade import Cidade


@dataclass
class ResultadoBusca:
    arvore_de_cidades: List[Cidade]
