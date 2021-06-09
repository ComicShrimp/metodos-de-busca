from typing import List
from cidade import Cidade


class CidadeMapa:
    cidade: Cidade
    cidades_adjascentes: List[Cidade]

    def __init__(self, cidade: Cidade, cidades_adjascentes: List[Cidade]) -> None:
        self.cidade = cidade
        self.cidades_adjascentes = cidades_adjascentes
