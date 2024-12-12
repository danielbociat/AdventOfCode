import os

script_dir = os.path.dirname(__file__)
rel_path = "input12.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

rows = len(mp)
cols = len(mp[0])

visited = [[False]*cols for _ in range(rows)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def inMatrix(i, j):
    return i >= 0 and j >= 0 and i < rows and j < cols 

area = 1
perimeter = 0

def fill(i, j):
    global area
    global perimeter
    visited[i][j] = True

    for k in range(4):
        new_i = i + di[k]
        new_j = j + dj[k]

        if not inMatrix(new_i, new_j) or mp[i][j] != mp[new_i][new_j]:
            perimeter = perimeter + 1
        elif inMatrix(new_i, new_j)  and not visited[new_i][new_j] and mp[i][j] == mp[new_i][new_j]:
            visited[new_i][new_j] = True
            area = area + 1        
            fill(new_i, new_j)

print(rows, cols)

total = 0

for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            
            area = 1
            perimeter = 0
            fill(i, j)
            print(mp[i][j], area, perimeter)
            total += area * perimeter

print(total)