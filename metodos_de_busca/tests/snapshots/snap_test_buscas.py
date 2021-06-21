# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_busca_em_largura busca_em_largura'] = [
    'Cidade: Arad, Custo: 366',
    'Cidade: Zerind, Custo: 374',
    'Cidade: Sibiu, Custo: 253',
    'Cidade: Timisoara, Custo: 329',
    'Cidade: Oradea, Custo: 380',
    'Cidade: Fagaras, Custo: 178',
    'Cidade: Rimnicu Vilcea, Custo: 193',
    'Cidade: Lugoj, Custo: 244',
    'Cidade: Bucharest, Custo: 0'
]

snapshots['test_busca_gulosa busca_gulosa'] = [
    'Cidade: Arad, Custo: 366',
    'Cidade: Zerind, Custo: 374',
    'Cidade: Oradea, Custo: 380',
    'Cidade: Sibiu, Custo: 253',
    'Cidade: Rimnicu Vilcea, Custo: 193',
    'Cidade: pitesti, Custo: 98',
    'Cidade: Bucharest, Custo: 0'
]

snapshots['test_busca_profunda busca_profunda'] = [
    'Cidade: Arad, Custo: 366',
    'Cidade: Zerind, Custo: 374',
    'Cidade: Oradea, Custo: 380',
    'Cidade: Sibiu, Custo: 253',
    'Cidade: Fagaras, Custo: 178',
    'Cidade: Bucharest, Custo: 0'
]
