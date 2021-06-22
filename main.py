from metodos_de_busca.buscas.a_estrela import BuscaAEstrela
from metodos_de_busca.buscas import (
    BuscaGulosa,
    BuscaProfunda,
    BuscaInputDto,
    BuscaEmLargura,
)
from metodos_de_busca.sociedade import Mapa
from metodos_de_busca.metricas import Tempo, Resultado

tempo = Tempo()
mapa = Mapa()
print("Partida: " + mapa.partida.nome)
print("Chegada: " + mapa.chegada.nome)

tempo.inicia_contagem()
resultado = BuscaProfunda().executa(
    BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
)
tempo.termina_contagem()

tempo.mostra_tempo(titulo="Busca Profunda")

Resultado().mostra_resultado(resultado, titulo="Busca Profunda")

mapa._limpa_busca()


# tempo.inicia_contagem()
# resultado = BuscaEmLargura().executa(
#     BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
# )
# tempo.termina_contagem()

# tempo.mostra_tempo(titulo="Busca Largura")

# Resultado().mostra_resultado(resultado, titulo="Busca Largura")

# mapa._limpa_busca()


tempo.inicia_contagem()
resultado = BuscaGulosa().executa(
    BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
)
tempo.termina_contagem()

tempo.mostra_tempo(titulo="Busca Gulosa")

Resultado().mostra_resultado(resultado, titulo="Busca Gulosa")

mapa._limpa_busca()

tempo.inicia_contagem()
resultado = BuscaAEstrela().executa(
    BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
)
tempo.termina_contagem()

tempo.mostra_tempo(titulo="Busca A*")

Resultado().mostra_resultado(resultado, titulo="Busca A*")

mapa._limpa_busca()

print(
    "\nObs: Os resultados são mostrados considerando o custo de heuristica e do caminho."
)
print(
    "Entretanto, a heuristica nã o é considerada na busca profunda e na busca em largura"
)
