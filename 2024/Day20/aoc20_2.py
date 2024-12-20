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


def in_map(i, j):
    return i >= 0 and j >= 0 and i < rows and j < cols and mp[i][j] != '#' 

inf = float('inf')

def fill(i, j):
    visited = defaultdict(lambda: inf)
    curr = 0

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

            if in_map(new_i, new_j) and visited[(new_i, new_j)] == inf:
                visited[(new_i, new_j)] = visited[(i,j)] +1
                q.append((new_i, new_j))
    
    return visited

start_dist = fill(start_i, start_j)
end_dist = fill(end_i, end_j)

init_sol = start_dist[(end_i, end_j)]

print(init_sol)

total = 0

def man_dist(i, j, ii, jj):
    return abs(i - ii) + abs(j - jj)

for i in range(rows):
    for j in range(cols):
        for ii in range(rows):
            for jj in range(cols):
                man_distance = man_dist(i, j, ii, jj)
                if man_distance <= 20:
                    sol = start_dist[(i,j)] + end_dist[(ii,jj)] + man_distance
                    if sol + 100 <= init_sol:
                        total += 1
                
print(total)
