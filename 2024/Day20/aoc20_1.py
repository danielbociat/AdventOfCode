import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input20.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()


rows = len(mp)
cols = len(mp[0])

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for i in range(rows):
    for j in range(cols):
        if mp[i][j] == 'S':
            start_i, start_j = i, j
        if mp[i][j] == 'E':
            end_i, end_j = i, j

cheat_i = -1
cheat_j = -1

def in_map(i, j):
    return i >= 0 and j >= 0 and i < rows and j < cols and (mp[i][j] != '#' or (i == cheat_i and j == cheat_j))

visited = defaultdict(lambda: -1)

def fill(i, j, curr):
    q = []
    q.append((i,j))
    visited[(i,j)] = curr

    while len(q) > 0:
        i,j = q.pop(0)
        # print(i,j)

        for k in range(4):
            di, dj = dir[k]

            new_i = i + di        
            new_j = j + dj

            if in_map(new_i, new_j) and visited[(new_i, new_j)] == -1:
                visited[(new_i, new_j)] = visited[(i,j)] +1
                q.append((new_i, new_j))

fill(start_i, start_j, 0)
init_sol = visited[(end_i, end_j)]

total = 0
for i in range(rows):
    for j in range(cols):
        if mp[i][j] == '#':
            visited = defaultdict(lambda: -1)
            cheat_i, cheat_j = i, j
            fill(start_i, start_j, 0)
            if visited[(end_i, end_j)] + 100 <= init_sol:
                total += 1
            cheat_i, cheat_j = -1, -1

print(total)