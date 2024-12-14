import os
import re

script_dir = os.path.dirname(__file__)
rel_path = "input14.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

robots = list()

for line in mp:
    A = re.split('=|,|\s', line)
    # print(A)

    robots.append({'p':[int(A[1]), int(A[2])], "v":[int(A[4]), int(A[5])]})

# print(robots)

rows = 103
cols = 101

# print(rows, cols)

T = 100

c = [0,0,0,0]

for robot in robots:
    robot['p'][0] = (robot['p'][0] + T*robot['v'][0]) % cols
    robot['p'][1] = (robot['p'][1] + T*robot['v'][1]) % rows

    if robot['p'][0] < cols//2 and robot['p'][1] < rows//2:
        c[0] += 1
    if robot['p'][0] > cols//2 and robot['p'][1] > rows//2:
        c[1] += 1
    if robot['p'][0] < cols//2 and robot['p'][1] > rows//2:
        c[2] += 1
    if robot['p'][0] > cols//2 and robot['p'][1] < rows//2:
        c[3] += 1

p = 1
for ci in c:
    p = p * ci

print(c)
print(p)