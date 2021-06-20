from metodos_de_busca.buscas import (
    BuscaAEstrela,
    BuscaGulosa,
    BuscaInputDto,
    BuscaProfunda,
)
from metodos_de_busca.sociedade import Mapa


def test_busca_profunda(snapshot):
    mapa = Mapa()

    resultado = BuscaProfunda().executa(
        BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
    )

    snapshot.assert_match(resultado.exporta(), "busca_profunda")


def test_busca_gulosa(snapshot):
    mapa = Mapa()

    resultado = BuscaGulosa().executa(
        BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
    )

    snapshot.assert_match(resultado.exporta(), "busca_gulosa")
