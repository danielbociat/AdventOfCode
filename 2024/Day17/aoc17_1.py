import os

script_dir = os.path.dirname(__file__)
rel_path = "input17.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

A = int((mp[0].split(':'))[1])
B = int((mp[1].split(':'))[1])
C = int((mp[2].split(':'))[1])

commands = [int(el) for el in (mp[4].split(":"))[1].split(",")]

out = list()

i = 0

def get_elem():
    global i
    v = commands[i] if commands[i] <= 3 else [A,B,C][commands[i] - 4]
    i += 1
    return v

while i < len(commands):
    flag = True
    instr = int(commands[i])

    i += 1

    match instr:
        case 0:
            A = A >> get_elem()
        
        case 1:
            B = B ^ int(commands[i])
            i += 1
        case 2:
            B = get_elem() % 8

        case 3:
            if A != 0:
                i = commands[i]
            else:
                i += 1

        case 4:
            B = B ^ C
            i += 1

        case 5:
            out.append(get_elem()%8)

        case 6:
            B = A >> get_elem() 

        case 7:
            C = A >> get_elem()

        case _:
            print("Oopsie daisy")
            break

print(",".join(map(str,out)))