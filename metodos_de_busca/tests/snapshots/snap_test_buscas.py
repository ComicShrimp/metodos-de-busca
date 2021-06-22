# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_busca_a_estrela busca_a_estrela'] = [
    'Cidade: Sibiu, heuristica: 253',
    'Cidade: Rimnicu Vilcea, heuristica: 193',
    'Cidade: pitesti, heuristica: 98',
    'Cidade: Bucharest, heuristica: 0'
]

snapshots['test_busca_gulosa busca_gulosa'] = [
    'Cidade: Sibiu, heuristica: 253',
    'Cidade: Fagaras, heuristica: 178',
    'Cidade: Bucharest, heuristica: 0'
]

snapshots['test_busca_profunda busca_profunda'] = [
    'Cidade: Zerind, heuristica: 374',
    'Cidade: Oradea, heuristica: 380',
    'Cidade: Sibiu, heuristica: 253',
    'Cidade: Fagaras, heuristica: 178',
    'Cidade: Bucharest, heuristica: 0'
]
