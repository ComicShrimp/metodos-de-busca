class Cidade:
    nome: str
    visitado: bool

    def __init__(self, nome: str, visitado: bool = False) -> None:
        self.nome = nome
        self.visitado = visitado
