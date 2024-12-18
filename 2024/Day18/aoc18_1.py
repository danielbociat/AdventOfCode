import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input18.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    bytes = f.read().splitlines()

map_size = 71
bytes_fallen = 1024

mp = [['.']*map_size for _ in range(map_size)]

for i in range(bytes_fallen):
    [ni, nj] = bytes[i].split(',')
    print(ni, nj)
    
    mp[int(nj)][int(ni)] = '#'

for i in range(map_size):
    for j in range(map_size):
        print(mp[i][j], end=' ')
    print()

start_i, start_j = 0, 0
end_i, end_j = map_size-1, map_size-1

def in_map(i, j):
    return i >=0 and j>=0 and i < map_size and j < map_size and mp[i][j] != '#'

d = [(-1,0), (1,0), (0,1), (0,-1)]
visited = defaultdict(lambda: -1)

def fill(i, j, curr):
    q = []
    q.append((i,j))
    visited[(i,j)] = curr

    while len(q) > 0:
        i,j = q.pop(0)
        # print(i,j)

        for k in range(4):
            di, dj = d[k]

            new_i = i + di        
            new_j = j + dj

            if in_map(new_i, new_j) and visited[(new_i, new_j)] == -1:
                visited[(new_i, new_j)] = visited[(i,j)] +1
                q.append((new_i, new_j))

        # print(q)

fill(0, 0, 0)

for i in range(map_size):
    for j in range(map_size):
        print(visited[(i,j)], end=' ')
    print()

print(visited[(end_i,end_j)])
