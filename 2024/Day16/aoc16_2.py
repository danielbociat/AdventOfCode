import os
import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

script_dir = os.path.dirname(__file__)
rel_path = "input16.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

rows = len(mp)
cols = len(mp[0])

for i in range(rows):
    for j in range(cols):
        if mp[i][j] == 'S':
            start_i, start_j = i,j 
        if mp[i][j] == 'E':
            end_i, end_j = i,j 

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def in_mat(i, j):
    return i >= 0 and j >= 0 and i < rows and j < cols and mp[i][j] != '#'

inf = float('inf')
DP = defaultdict(lambda: inf)


def solve(i, j, o, score):
    if DP[(i,j,o)] <= score:
        return 
    
    DP[(i,j,o)] = score
    solve(i, j, (o + 1)%4, score+1000)
    solve(i, j, (o + 3)%4, score+1000)

    di, dj = dir[o]
    new_i = i + di
    new_j = j + dj

    if in_mat(new_i, new_j):
        solve(new_i, new_j, o, score + 1)

solve(start_i, start_j, 0, 0)

ans = min(DP[(end_i,end_j,0)], DP[(end_i,end_j,1)], DP[(end_i,end_j,2)], DP[(end_i,end_j,3)])

print("Part 1 - DONE")

# END SOL 1

def solve2(i, j, o, score, mark):
    if DP2[mark][(i,j,o)] <= score:
        return 
    
    DP2[mark][(i,j,o)] = score
    solve2(i, j, (o + 1)%4, score+1000, mark)
    solve2(i, j, (o + 3)%4, score+1000, mark)

    di, dj = dir[o]
    new_i = i + di
    new_j = j + dj

    if in_mat(new_i, new_j):
        solve2(new_i, new_j, o, score + 1, mark)

DP2 = [defaultdict(lambda: inf) for _ in range(4)]

poss = list()

for d in range(4):
    if DP[(end_i,end_j,d)] == ans:
        solve2(end_i, end_j, (d+2)%4, 0, (d+2)%4)
        poss.append((d+2)%4)

print("Part 2 - Precompute - DONE")

s = set()
for i in range(rows):
    for j in range(cols):
        best = inf
        for k in range(4):
            for v in poss:
                dist1 = DP[(i,j,k)]
                dist2 = DP2[v][(i,j,(k+2)%4)]
                best = min(best, dist1 + dist2)

        if best == ans:
            s.add((i,j))

print("Part 2 - DONE")

print(len(s))
        
