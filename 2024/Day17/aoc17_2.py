from itertools import *
from collections import *
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

def get_elem(A, B, C, commands):
    global idx
    v = commands[idx] if commands[idx] <= 3 else [A,B,C][commands[idx] - 4]
    idx += 1
    return v

idx = 0
def solve(A, B, C, commands):
    global idx
    out = list()
    while idx < len(commands):
        flag = True
        instr = int(commands[idx])

        idx += 1

        match instr:
            case 0:
                A = A >> get_elem(A, B, C, commands)
            
            case 1:
                B = B ^ int(commands[idx])
                idx += 1
            case 2:
                B = get_elem(A, B, C, commands) % 8

            case 3:
                if A != 0:
                    idx = commands[idx]
                else:
                    idx += 1

            case 4:
                B = B ^ C
                idx += 1

            case 5:
                out.append(get_elem(A, B, C, commands)%8)

            case 6:
                B = A >> get_elem(A, B, C, commands) 

            case 7:
                C = A >> get_elem(A, B, C, commands)

            case _:
                print("Oopsie daisy")
                break
    return out

cands=[0]

for p in range(len(commands)):
    lo=1 if p == 0 else 0
    ncands=[]
    for ans in cands:
        for i in range(lo,8):
            idx = 0
            val = ans + i * 8**(len(commands)-p-1)
            if solve(val, 0, 0, commands)[~p] == commands[~p]:
                ncands.append(val)
    cands = ncands

print(min(cands))