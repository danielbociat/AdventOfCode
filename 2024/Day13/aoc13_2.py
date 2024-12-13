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
    TG_X = int(C[1]) + 10000000000000
    TG_Y = int(C[-1]) + 10000000000000

    b = (TG_Y - TG_X * Y1 / X1) / (Y2 - (X2 * Y1) / X1)
    a = (TG_X - b * X2) / X1

    a = round(a)
    b = round(b)

    if X1 * a + X2 * b == TG_X and Y1 * a + Y2 * b == TG_Y:
        total += (3*a + b)
        
print(total)