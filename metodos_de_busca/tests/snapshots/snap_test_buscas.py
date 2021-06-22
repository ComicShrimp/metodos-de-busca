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

snapshots['test_busca_em_largura busca_em_largura'] = [
    'Cidade: Zerind, heuristica: 374',
    'Cidade: Sibiu, heuristica: 253',
    'Cidade: Timisoara, heuristica: 329',
    'Cidade: Oradea, heuristica: 380',
    'Cidade: Arad, heuristica: 366',
    'Cidade: Lugoj, heuristica: 244',
    'Cidade: Arad, heuristica: 366',
    'Cidade: Mehadia, heuristica: 241',
    'Cidade: Dobreta, heuristica: 242',
    'Cidade: Craiova, heuristica: 160',
    'Cidade: pitesti, heuristica: 98',
    'Cidade: Rimnicu Vilcea, heuristica: 193',
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
