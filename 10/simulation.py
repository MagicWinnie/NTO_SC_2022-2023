import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
from random import random

adj_list = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
]
adj_matrix = np.array(adj_list, dtype=np.uint8)


P = 1 - 0.999948708021091
N = 1000
START = 0
END = 13
EDGES = [
    (0, 1),
    (1, 2),
    (1, 4),
    (3, 4),
    (3, 7),
    (4, 5),
    (6, 7),
    (7, 8),
    (8, 11),
    (8, 9),
    (9, 10),
    (10, 13),
    (11, 12),
    (12, 13)
]


G_original = nx.from_numpy_matrix(adj_matrix)
# pos = nx.spring_layout(G_original, seed=100)
# nx.draw(G, pos=pos, with_labels=True)
# plt.show()

mean_time = 0
for _ in tqdm(range(N)):
    G = G_original.copy() # type: ignore
    i = 0
    while True:
        for e in EDGES:
            if random() < P and G.has_edge(*e): # type: ignore
                G.remove_edge(*e) # type: ignore
        if not nx.has_path(G, START, END):
            mean_time += i
            break
        i += 1
print(mean_time / N, "H")
print(round(mean_time / N / 10) * 10)
