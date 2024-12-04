import os

total = 0

def in_matrix(i,j,n,m):
    return 0 <= i and i < n and 0 <= j and j < m

def find_xmas(i,j,idx, di, dj):
    if not in_matrix(i,j,n,m):
        return 0
    
    if lines[i][j] == xmas[idx]:
        if idx == 0:
            return find_xmas(i-1,j,idx+1, -1, 0) + find_xmas(i-1,j-1,idx+1, -1, -1) + \
                    find_xmas(i,j-1,idx+1, 0, -1) + find_xmas(i+1,j,idx+1, 1, 0) + \
                    find_xmas(i+1,j+1,idx+1, 1, 1) + find_xmas(i,j+1,idx+1, 0, 1) + \
                    find_xmas(i-1,j+1,idx+1, -1, 1) + find_xmas(i+1,j-1,idx+1, 1, -1) 
        elif idx == 3:
            return 1
        else:
            return find_xmas(i + di, j + dj, idx+1, di, dj)
    
    return 0
        

xmas = "XMAS"

script_dir = os.path.dirname(__file__)
rel_path = "input4.txt"
abs_file_path = os.path.join(script_dir, rel_path)

lines = []
with open(abs_file_path) as f:
    for line in f:
        lines.append(line)

n = len(lines)
m = len(lines[0]) - 1


for i in range(n):
    for j in range(m):
        total += find_xmas(i,j,0, 0, 0)

print(total)