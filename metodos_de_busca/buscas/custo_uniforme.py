from typing import List

from metodos_de_busca.sociedade import Cidade

from .busca import IBusca, BuscaInputDto, ResultadoBusca


class Folha:
    def __init__(
        self, pilha: List[Cidade] = [], custo_total: int = 0, finalizou: bool = False
    ) -> None:
        self.pilha = pilha
        self.custo_total = custo_total
        self.finalizou = finalizou


class BuscaDeCustoUniforme(IBusca):  # A*
    def __init__(self):
        self.folhas: List[Folha] = []
        self.arvore_de_busca: List[Cidade] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        if self.folhas == []:
            self.folhas.append(
                Folha(
                    pilha=[input_dto.partida],
                    custo_total=0,
                    finalizou=False,
                )
            )

        if self.folhas_terminaram():
            folha_menor_custo = self.achar_folha_menor_custo()
            return ResultadoBusca(
                arvore_de_cidades=self.arvore_de_busca, caminho=folha_menor_custo.pilha
            )

        folha_menor_custo = self.achar_folha_menor_custo()
        self.folhas.remove(folha_menor_custo)
        folha_menor_custo.pilha[-1].visitar()
        self.arvore_de_busca.append(folha_menor_custo.pilha[-1])

        for cidade in folha_menor_custo.pilha[-1].vizinhos:
            if not cidade.cidade_destino.foi_visitado():
                custo_total = cidade.custo_do_caminho

                destino = False
                if cidade.cidade_destino.nome == input_dto.chegada.nome:
                    destino = True

                self.folhas.append(
                    Folha(
                        pilha=(folha_menor_custo.pilha + [cidade.cidade_destino]),
                        custo_total=custo_total,
                        finalizou=destino,
                    )
                )

        return self.executa(input_dto=input_dto)

    def achar_folha_menor_custo(self) -> Folha:
        menor_custo = self.folhas[0]

        for folha in self.folhas:
            if folha.custo_total < menor_custo.custo_total and not folha.finalizou:
                menor_custo = folha

        return menor_custo

    def folhas_terminaram(self):

        for folha in self.folhas:
            if not folha.finalizou:
                return False

        return True
