from metodos_de_busca.buscas.custo_uniforme import BuscaDeCustoUniforme
from metodos_de_busca.buscas import BuscaGulosa, BuscaProfunda, BuscaInputDto
from metodos_de_busca.sociedade import Mapa
from metodos_de_busca.metricas import Tempo

tempo = Tempo()
mapa = Mapa()
print("Partida: " + mapa.partida.nome)
print("Chegada: " + mapa.chegada.nome)


tempo.inicia_contagem()
print("\nBusca Profunda\n")
resultado = BuscaProfunda().executa(
    BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
)
tempo.termina_contagem()

print("\n\n")
print(tempo.tempo_total())
print("\n\n")

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

print("\n\nBusca Custo Uniforme\nCaminho encontrado: ")
resultado = BuscaDeCustoUniforme().executa(
    BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
)

print(resultado.caminho_nao_encontrado)

for cidade in resultado.arvore_de_cidades:
    print(cidade.nome)

print("\n\n")
custo = 0
for cidade in resultado.caminho:
    print(cidade.nome)

mapa._limpa_busca()
