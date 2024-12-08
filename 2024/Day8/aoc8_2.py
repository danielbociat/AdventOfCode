import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input8.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

antenna_map = defaultdict(lambda: list())
for i in range(len(mp)):
    for j in range(len(mp[i])):
        if mp[i][j] != '.':
            antenna_map[mp[i][j]].append((i,j))

antinodes = set()

keys = antenna_map.keys()

def isValid(tpl):
    return tpl[0] >= 0 and tpl[1] >= 0 and tpl[0] < len(mp) and tpl[1] < len(mp[0])

for key in keys:
    for i in range(len(antenna_map[key])):
        for j in range(i+1, len(antenna_map[key])):
            print(key, antenna_map[key][i], antenna_map[key][j])

            delta = (antenna_map[key][i][0] - antenna_map[key][j][0], antenna_map[key][i][1] - antenna_map[key][j][1])
            print(delta)

            new_tlp = (antenna_map[key][i][0], antenna_map[key][i][1])
            while isValid(new_tlp):
                print(new_tlp) 
                antinodes.add(new_tlp)
                new_tlp = (new_tlp[0] + delta[0], new_tlp[1] + delta[1])
            
            new_tlp2 = (antenna_map[key][j][0], antenna_map[key][j][1])
            while isValid(new_tlp2) :
                print(new_tlp2) 
                antinodes.add(new_tlp2)
                new_tlp2 = (new_tlp2[0] - delta[0], new_tlp2[1] - delta[1])
            
            print()

for i in range(len(mp)):
    for j in range(len(mp[i])):
        if ((i,j) in antinodes) and mp[i][j] == '.':
            print('#', end='')
        else:
            print(mp[i][j], end='')
    print()

print(len(antinodes))