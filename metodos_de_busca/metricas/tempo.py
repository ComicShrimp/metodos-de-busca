import time


class Tempo:
    def __init__(self) -> None:
        self.inicial = 0
        self.final = 0

    def inicia_contagem(self):
        self.inicial = time.time()

    def termina_contagem(self):
        self.final = time.time()

    def mostra_tempo(self, titulo: str = None):
        diferenca = (self.final - self.inicial) * 1000 * 1000
        (millisegundos, microsegundos) = divmod(diferenca, 1000)
        (segundos, millisegundos) = divmod(millisegundos, 1000)

        if titulo is None:
            return (
                "Tempo total: {} segundos | {} millisegundos | {} microsegundos".format(
                    segundos, millisegundos, microsegundos
                )
            )
        else:
            print(
                "{} - Tempo total: {} segundos | {} millisegundos | {} microsegundos\n".format(
                    titulo, segundos, millisegundos, microsegundos
                )
            )
