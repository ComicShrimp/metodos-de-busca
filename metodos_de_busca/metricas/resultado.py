from metodos_de_busca.buscas import ResultadoBusca


class Resultado:
    def __init__(self) -> None:
        pass

    def mostra_resultado(self, resultado: ResultadoBusca, titulo: str):
        print("Resultado para {}\n".format(titulo))

        if not resultado.caminho_nao_encontrado:
            print("\nArvore de Busca\n")

            interator = 0
            for cidade in resultado.arvore_de_cidades:
                interator = interator + 1
                print(
                    "{} - {}: H={} D={}".format(
                        interator,
                        cidade.cidade_destino.nome,
                        cidade.cidade_destino.heuristica,
                        cidade.custo_do_caminho,
                    )
                )

            print("\nCaminho Ideal:\n")

            interator = 0
            custo_total = 0
            if resultado.caminho is not None:
                for cidade in resultado.caminho:
                    interator = interator + 1
                    custo_total = cidade.custo_do_caminho + custo_total
                    print(
                        "{} - {}: custo={}".format(
                            interator,
                            cidade.cidade_destino.nome,
                            cidade.custo_do_caminho,
                        )
                    )

                print("\nCusto Total (Distância Percorrida): {}\n".format(custo_total))

        else:
            print("\nNenhum caminho encontrado\n")
