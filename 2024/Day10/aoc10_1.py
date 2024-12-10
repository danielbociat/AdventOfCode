import os

script_dir = os.path.dirname(__file__)
rel_path = "input10.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()
    mp = [[int(el) for el in line ] for line in mp]

rows = len(mp)
cols = len(mp[0])

def inGrid(i, j):
    return i >=0 and j>=0 and i < rows and j < cols

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def count_score(curr_i, curr_j):
    val = mp[curr_i][curr_j]

    if val == 9:
        if (curr_i, curr_j) in visited:
            return 0
        visited.add((curr_i, curr_j))
        return 1
    
    ret = 0
    for k in range(4):
        new_i = curr_i + di[k]
        new_j = curr_j + dj[k]

        if inGrid(new_i, new_j) and mp[new_i][new_j] == val + 1:
            ret += count_score(new_i, new_j)

    return ret



total = 0
for i in range(rows):
    for j in range(cols):
        if mp[i][j] == 0:
            visited = set()
            ret =  count_score(i, j)
            #print(ret, i, j)
            total += ret

print(total)