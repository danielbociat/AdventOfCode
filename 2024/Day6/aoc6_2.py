import os
import copy
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input6.txt"
abs_file_path = os.path.join(script_dir, rel_path)

i = 0
j = 0
start_i = -1
start_j = -1


with open(abs_file_path) as f:
    mp = f.read().splitlines()

mp = [list(line) for line in mp]

for line in mp:
    if start_i == -1:
        for j in range(len(line)):
            if line[j] == '^':
                start_i = i
                start_j = j
                break
    
    i+=1

rows = len(mp)
cols = len(mp[0]) 

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr_dir = 0

total = 0

def in_map(si, sj):
    return  si >= 0 and si < rows and sj >= 0 and sj < cols


new_mp = copy.deepcopy(mp)
for i in range(rows):
    for j in range(cols):
        if mp[i][j] != '.':
            continue
        
        new_mp[i][j] = '#'
        spaces_visited = set()
        curr_dir = 0
        si = start_i
        sj = start_j


        is_loop = False
        while in_map(si, sj):
            if (si,sj,curr_dir) in spaces_visited:
                is_loop = True
                break
            else:
                spaces_visited.add((si,sj,curr_dir))

            new_si = si + dirs[curr_dir][0]
            new_sj = sj + dirs[curr_dir][1] 

            if in_map(new_si, new_sj) and new_mp[new_si][new_sj] == '#':
                curr_dir = (curr_dir + 1)%4
            else:
                si = new_si
                sj = new_sj

        new_mp[i][j] = '.'

        if is_loop:
            total+=1

print(total)