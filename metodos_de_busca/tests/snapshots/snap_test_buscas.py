# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_busca_gulosa busca_gulosa'] = [
    GenericRepr('Arad'),
    GenericRepr('Zerind'),
    GenericRepr('Oradea'),
    GenericRepr('Sibiu'),
    GenericRepr('Rimnicu Vilcea'),
    GenericRepr('pitesti'),
    GenericRepr('Bucharest')
]

snapshots['test_busca_profunda busca_profunda'] = [
    GenericRepr('Arad'),
    GenericRepr('Zerind'),
    GenericRepr('Oradea'),
    GenericRepr('Sibiu'),
    GenericRepr('Fagaras'),
    GenericRepr('Bucharest')
]
