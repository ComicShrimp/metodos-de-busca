from metodos_de_busca.buscas import ResultadoBusca


class Resultado:
    def __init__(self) -> None:
        pass

    def mostra_resultado(self, resultado: ResultadoBusca, titulo: str):
        print("\nResultado para {}\n".format(titulo))

        print("\nArvore de Busca\n")

        interator = 0
        for cidade in resultado.arvore_de_cidades:
            print("{} - {}: {}".format(interator, cidade.nome, 0))
