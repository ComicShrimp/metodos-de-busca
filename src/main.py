from mapa import Mapa

mapa = Mapa()
print("Partida: " + str(mapa.cidades[0]["nome"]))
print("Destino: " + str(mapa.cidades[1]["nome"]))
print(mapa.busca_profunda(mapa.cidades[0], mapa.cidades[1]))
