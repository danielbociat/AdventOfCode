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
    robots.append({'p':[int(A[1]), int(A[2])], "v":[int(A[4]), int(A[5])]})

rows = 103
cols = 101

T = rows*cols

for i in range(T):
    grid = [[' '] * cols for _ in range(rows)]

    for robot in robots:
        nx = (robot['p'][0] + i * robot['v'][0]) % cols
        ny = (robot['p'][1] + i * robot['v'][1]) % rows
        grid[ny][nx] = '#'

    grid = '\n'.join(''.join(line) for line in grid)

    if '###########' in grid:
        print(grid)
        print(i)
        break