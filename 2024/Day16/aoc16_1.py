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

print(min(DP[(end_i,end_j,0)], DP[(end_i,end_j,1)], DP[(end_i,end_j,2)], DP[(end_i,end_j,3)]))
