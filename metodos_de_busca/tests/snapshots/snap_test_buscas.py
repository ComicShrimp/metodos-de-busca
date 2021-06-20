# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_busca_a_estrela busca_a_estrela'] = [
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
