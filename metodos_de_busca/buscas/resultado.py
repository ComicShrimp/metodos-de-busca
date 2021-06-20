from dataclasses import dataclass
from typing import List, Optional

from metodos_de_busca.sociedade import Cidade


@dataclass
class ResultadoBusca:
    arvore_de_cidades: Optional[List[Cidade]] = None
    caminho_impossivel: bool = False
