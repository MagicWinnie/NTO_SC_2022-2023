import networkx as nx

G = nx.Graph()

n, m = map(int, input().split())
used = set()
for _ in range(m):
    v, u = map(int, input().split())
    used.add(v)
    used.add(u)
    G.add_edge(v, u)

count_one = 0
for i in used:
    count_one += G.degree[i] == 1

print((count_one + 1) // 2)
