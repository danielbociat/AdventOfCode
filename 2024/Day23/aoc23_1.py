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

total = 0

for node1 in nodes:
    for node2 in graph[node1]:
        for node3 in graph[node1]:
            if node2 in graph[node3]:
                if node1[0] == 't' or  node2[0] == 't' or  node3[0] == 't':
                    print(node1,node2,node3)
                    total += 1

print(total // 6)