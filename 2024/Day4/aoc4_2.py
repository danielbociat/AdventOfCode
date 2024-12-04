import os

total = 0

def in_matrix(i,j,n,m):
    return 0 <= i and i < n and 0 <= j and j < m

def find_x_mas(i,j,idx):
    if not in_matrix(i,j,n,m):
        return 0
    
    if lines[i][j] == x_mas[idx]:
        if idx == 1:
            if not ((find_x_mas(i-1, j-1, idx-1) and find_x_mas(i+1, j+1, idx+1)) or (find_x_mas(i-1, j-1, idx+1) and find_x_mas(i+1, j+1, idx-1))):
                return 0
            
            if not ((find_x_mas(i+1, j-1, idx-1) and find_x_mas(i-1, j+1, idx+1)) or (find_x_mas(i+1, j-1, idx+1) and find_x_mas(i-1, j+1, idx-1))):
                return 0

            return 1

        else:
            return 1
     
    return 0
        

x_mas = "MAS"

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
        total += find_x_mas(i,j, 1)

print(total)