import os

script_dir = os.path.dirname(__file__)
rel_path = "input9.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    line = f.read().splitlines()[0]

is_free = False
id = 0
mem = list()
for char in line:
    num = int(char)

    if(is_free):
        mem.append(['.', num])
    else:
        mem.append([id, num])
        id+=1

    is_free = not is_free

right = len(mem) - 1
while right >= 0:
    while mem[right][0] == '.':
        right-=1
    
    size = mem[right][1]
    sym =  mem[right][0]

    for left in range(right):
        if mem[left][0] == '.' and mem[left][1] >= size:
            mem[right] = ['.', size]
            if mem[left][1] > size:
                mem[left][1] -= size
                mem.insert(left, [sym, size])
                
            else:
                mem[left][0] = sym
            
            break
    
    right -= 1


sol = 0
curr_block = 0

for i in range(len(mem)):
    for j in range(mem[i][1]):
        if mem[i][0] != '.':
            sol += mem[i][0] * curr_block
        curr_block+=1


print(sol)