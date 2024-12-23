import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input23.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

graph = defaultdict(lambda: list())

for conn in mp:
    pcs = conn.split("-")

    graph[pcs[0]].append(pcs[1])
    graph[pcs[1]].append(pcs[0])

print(graph)

nodes = list(graph.keys())
print(nodes)
nodes = sorted(nodes)

best_len = 0
for node in nodes:
    clique = [node]
    base = [sorted([el for el in graph[node]], reverse=True)]

    while base:
        if not base[-1]:
            clique.pop()
            base.pop()
            continue

        el = base[-1].pop()
        clique.append(el)

        if len(clique) > best_len:
            best_sol = clique.copy()
            best_len = len(clique)

        base.append(sorted({*base[-1]}&{el2 for el2 in graph[el] if el2 > el}, reverse=True))

print(",".join(sorted(best_sol)))
        
