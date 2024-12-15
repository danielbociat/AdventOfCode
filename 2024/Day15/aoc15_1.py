import os
import re

script_dir = os.path.dirname(__file__)
rel_path = "input15.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

mp = [list(line) for line in mp]

sz = 50


moves = {
    "^": [-1, 0],
    "v": [1, 0],
    "<": [0, -1],
    ">": [0, 1]
    }


for i in range(sz):
    for j in range(len(mp[0])):
        if mp[i][j] == '@':
            curr_i = i
            curr_j = j
            break
    
for line in mp[:sz]:
    print(line)
print()

for command in mp[sz+1:]:
    for move in command:
        print(curr_i, curr_j, move)
        new_i = curr_i + moves[move][0]
        new_j = curr_j + moves[move][1]

        if mp[new_i][new_j] == '.':
            mp[curr_i][curr_j] = '.'
            curr_i = new_i
            curr_j = new_j
            mp[curr_i][curr_j] = '@'

        elif mp[new_i][new_j] == 'O':
            box_i = new_i
            box_j = new_j

            while mp[box_i][box_j] == 'O':
                box_i = box_i + moves[move][0]
                box_j = box_j + moves[move][1]

            if mp[box_i][box_j] == '.':
                mp[box_i][box_j] = 'O'
                mp[curr_i][curr_j] = '.'
                curr_i = new_i
                curr_j = new_j
                mp[curr_i][curr_j] = '@'
    
        # for line in mp[:sz]:
        #     print(line)
        # print()

total = 0
for i in range(sz):
    for j in range(len(mp[0])):
        if mp[i][j] == 'O':
            total = total + 100*i + j

print(total)