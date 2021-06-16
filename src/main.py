from mapa import Mapa

mapa = Mapa()
print("Partida: " + mapa.cidades[0].nome)
print("Destino: " + mapa.cidades[1].nome)

print("\nBusca Profunda\nCaminho encontrado: ")
resultado = mapa.busca_profunda(mapa.cidades[0], mapa.cidades[1])

for cidade in resultado:
    print(cidade.nome)

mapa._limpa_busca()

print("\n\nBusca Gulosa\nCaminho encontrado: ")
resultado = mapa.busca_gulosa(mapa.cidades[0], mapa.cidades[1])

for cidade in resultado:
    print(cidade.nome)

mapa._limpa_busca()
