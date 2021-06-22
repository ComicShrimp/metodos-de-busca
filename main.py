from metodos_de_busca.buscas.a_estrela import BuscaAEstrela
from metodos_de_busca.buscas.custo_uniforme import BuscaDeCustoUniforme
from metodos_de_busca.buscas import BuscaGulosa, BuscaProfunda, BuscaInputDto
from metodos_de_busca.sociedade import Mapa
from metodos_de_busca.metricas import Tempo

tempo = Tempo()
mapa = Mapa()
print("Partida: " + mapa.partida.nome)
print("Chegada: " + mapa.chegada.nome)
print("\n\n")

tempo.inicia_contagem()
resultado = BuscaProfunda().executa(
    BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
)
tempo.termina_contagem()

tempo.mostra_tempo(titulo="Busca Profunda")

for cidade in resultado.arvore_de_cidades:
    print(cidade.nome)


mapa._limpa_busca()


print("\n\nBusca Gulosa\nCaminho encontrado: ")
resultado = BuscaGulosa().executa(
    BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
)

for cidade in resultado.arvore_de_cidades:
    print(cidade.nome)

mapa._limpa_busca()


print("\n\nBusca A*\nCaminho encontrado: ")
resultado = BuscaAEstrela().executa(
    BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
)

for cidade in resultado.arvore_de_cidades:
    print(cidade.nome)

mapa._limpa_busca()
