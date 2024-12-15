import os
from collections import deque

script_dir = os.path.dirname(__file__)
rel_path = "input15.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

mp = [list(line) for line in mp]

sz = 50
new_mp = list()

moves = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
    }

for i in range(sz):
    new_ln = list()
    for j in range(len(mp[0])):

        if mp[i][j] == "#":
            new_ln.append('#')
            new_ln.append('#')
        if mp[i][j] == ".":
            new_ln.append('.')
            new_ln.append('.')
        if mp[i][j] == "@":
            new_ln.append('@')
            new_ln.append('.')
        if mp[i][j] == "O":
            new_ln.append('[')
            new_ln.append(']')
        
    new_mp.append(new_ln.copy())


for line in new_mp:
    print(''.join(line))

for i in range(sz):
    for j in range(len(new_mp[0])):
        if new_mp[i][j] == '@':
            curr_i = i
            curr_j = j
            new_mp[i][j] = '.'
            break

R = len(new_mp)
C = len(new_mp[0])

r,c = curr_i,curr_j
for inst_line in mp[sz+1:]:
    for inst in inst_line:
        dr,dc = moves[inst]

        rr,cc = r+dr,c+dc

        if new_mp[rr][cc]=='#':
            continue

        elif new_mp[rr][cc]=='.':
            r,c = rr,cc

        elif new_mp[rr][cc] in ['[', ']', 'O']:
            Q = deque([(r,c)])
            SEEN = set()
            ok = True
            while Q:
                rr,cc = Q.popleft()
                if (rr,cc) in SEEN:
                    continue
                SEEN.add((rr,cc))
                rrr,ccc = rr+dr, cc+dc
                if new_mp[rrr][ccc]=='#':
                    ok = False
                    break
                if new_mp[rrr][ccc] == 'O':
                    Q.append((rrr,ccc))
                if new_mp[rrr][ccc]=='[':
                    Q.append((rrr,ccc))
                    assert new_mp[rrr][ccc+1]==']'
                    Q.append((rrr,ccc+1))
                if new_mp[rrr][ccc]==']':
                    Q.append((rrr,ccc))
                    assert new_mp[rrr][ccc-1]=='['
                    Q.append((rrr,ccc-1))
            if not ok:
                continue
            while len(SEEN) > 0:
                for rr,cc in sorted(SEEN):
                    rrr,ccc = rr+dr,cc+dc
                    if (rrr,ccc) not in SEEN:
                        assert new_mp[rrr][ccc] == '.'
                        new_mp[rrr][ccc] = new_mp[rr][cc]
                        new_mp[rr][cc] = '.'
                        SEEN.remove((rr,cc))
            r = r+dr
            c = c+dc

ans = 0
for r in range(R):
    for c in range(C):
        if new_mp[r][c] == '[':
            ans += 100*r+c


print(ans)