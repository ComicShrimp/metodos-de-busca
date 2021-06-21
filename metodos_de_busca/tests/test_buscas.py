from metodos_de_busca.buscas import (
    BuscaAEstrela,
    BuscaGulosa,
    BuscaInputDto,
    BuscaProfunda,
    BuscaEmLargura,
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


def test_busca_em_largura(snapshot):
    mapa = Mapa()

    resultado = BuscaEmLargura().executa(
        BuscaInputDto(partida=mapa.partida, chegada=mapa.chegada)
    )

    snapshot.assert_match(resultado.exporta(), "busca_em_largura")


def test_busca_a_estrela(snapshot):
    mapa = Mapa()

    resultado = BuscaAEstrela().executa(
        BuscaInputDto(
            partida=mapa.partida, chegada=mapa.chegada, heuristica=mapa.get_heuristica()
        )
    )

    snapshot.assert_match(resultado.exporta(), "busca_a_estrela")
