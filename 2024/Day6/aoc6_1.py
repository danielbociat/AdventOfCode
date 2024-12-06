import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input6.txt"
abs_file_path = os.path.join(script_dir, rel_path)

i = 0
j = 0
si = -1
sj = -1


with open(abs_file_path) as f:
    mp = f.read().splitlines()

mp = [list(line) for line in mp]

for line in mp:
    if si == -1:
        for j in range(len(line)):
            if line[j] == '^':
                si = i
                sj = j
                break
    
    i+=1

rows = len(mp)
cols = len(mp[0]) 

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
curr_dir = 0

total = 0

def in_map(si, sj):
    return  si >= 0 and si < rows and sj >= 0 and sj < cols

while in_map(si, sj):
    if mp[si][sj] != 'X':
        total += 1
        mp[si][sj] = 'X'

    new_si = si + dirs[curr_dir][0]
    new_sj = sj + dirs[curr_dir][1] 

    if in_map(new_si, new_sj) and mp[new_si][new_sj] == '#':
        curr_dir = (curr_dir + 1)%4
    else:
        si = new_si
        sj = new_sj

for line in mp:
    print(line)

print(total)