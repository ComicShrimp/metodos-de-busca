from typing import List
from cidade import Cidade


class CidadeMapa:
    cidade: Cidade

    def __init__(self, cidade: Cidade) -> None:
        self.cidade = cidade

    class Cidade:
        nome: str
        visitado: bool
        cidades_adjascentes: List[CidadeMapa]

        def __init__(
            self,
            nome: str,
            cidades_adjascentes: List[CidadeMapa],
            visitado: bool = False,
        ) -> None:
            self.nome = nome
            self.visitado = visitado
            self.cidades_adjascentes = cidades_adjascentes
