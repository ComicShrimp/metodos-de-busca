from typing import List
import copy

from metodos_de_busca.sociedade import Cidade, Vizinho

from .busca import IBusca, BuscaInputDto, ResultadoBusca


class Folha:
    def __init__(self, pilha: List[Vizinho] = []) -> None:
        self.pilha = pilha


class BuscaEmLargura(IBusca):
    def __init__(self):
        self.arvore_de_busca: List[Vizinho] = []
        self.folhas: List[Folha] = []

    def executa(self, input_dto: BuscaInputDto) -> ResultadoBusca:
        if self.folhas == []:
            for vizinho in input_dto.partida.vizinhos:
                self.folhas.append(Folha(pilha=[vizinho]))

        for folha in self.folhas:
            self.arvore_de_busca.append(folha.pilha[-1])
            folha.pilha[-1].cidade_destino.visitar()

            if folha.pilha[-1].cidade_destino.nome == input_dto.chegada.nome:
                return ResultadoBusca(
                    arvore_de_cidades=self.arvore_de_busca, caminho=folha.pilha
                )

        folhas_auxiliar = []

        for folha in self.folhas:
            self.folhas.remove(folha)

            for filha in folha.pilha[-1].cidade_destino.vizinhos:
                if not filha.cidade_destino.foi_visitado():
                    folhas_auxiliar.append(Folha(pilha=folha.pilha + [filha]))

        self.folhas = folhas_auxiliar

        return self.executa(input_dto=input_dto)
