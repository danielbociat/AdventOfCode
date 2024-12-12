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

def isBorder(i, j):
    for k in range(4):
        new_i = i + di[k]
        new_j = j + dj[k]

        if not inMatrix(new_i, new_j) or mp[i][j] != mp[new_i][new_j]:
            return True
        
    return False

def isConsecEdge(i, j, new_i, new_j):
    if abs(new_i - i) + abs(new_j - j) != 1:
        return 0

    res = 0
    for k in range(4):
        inMat1 = inMatrix(i+di[k], j+dj[k])
        inMat2 = inMatrix(new_i+di[k], new_j+dj[k])
        if not inMat1 and not inMat2:
            res += 1 
        if inMat1 and inMat2 and mp[i+di[k]][j+dj[k]] != mp[i][j] and mp[new_i+di[k]][new_j+dj[k]] != mp[new_i][new_j]:
            res +=1
        
    return res

area = 1
perimeter = 0

def fill(i, j):
    global area
    global perimeter

    visited[i][j] = True
    visi.add((i,j))

    for k in range(4):
        new_i = i + di[k]
        new_j = j + dj[k]

        if not inMatrix(new_i, new_j) or mp[i][j] != mp[new_i][new_j]:
            perimeter += 1
        elif inMatrix(new_i, new_j)  and not visited[new_i][new_j] and mp[i][j] == mp[new_i][new_j]:
            visited[new_i][new_j] = True
            area += 1        
            fill(new_i, new_j)

total = 0
visi = set()

for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            area = 1
            perimeter = 0
            consec_edges = 0

            visi.clear()
            fill(i, j)

            for pair1 in visi:
                for pair2 in visi:
                    if pair1 != pair2:
                        consec_edges += isConsecEdge(pair1[0], pair1[1], pair2[0], pair2[1])

            #  print(mp[i][j], area, perimeter, consec_edges//2)

            total += area * (perimeter-consec_edges//2)

print(total)