import os
import re

script_dir = os.path.dirname(__file__)
rel_path = "input13.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

total = 0
for i in range(0,len(mp), 4):
    A = re.split('\+|,', mp[i])
    B = re.split('\+|,', mp[i+1])

    X1 = int(A[1])
    Y1 = int(A[-1])

    X2 = int(B[1])
    Y2 = int(B[-1])

    C = re.split('=|,', mp[i+2])
    TG_X = int(C[1])
    TG_Y = int(C[-1])

    min_sol = 401
    for i in range(101):
        j1 = (TG_X - i*X1) / X2
        j2 = (TG_Y - i*Y1) / Y2

        if j1 == j2 and j1.is_integer() and j1 >= 0 and j1 <= 100:
            min_sol = min(min_sol, 3*i + j1)

    if min_sol < 401:
        total += int(min_sol)
        
print(total)