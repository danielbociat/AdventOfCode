import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
rel_path = "input21.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
    mp = f.read().splitlines()

key_locations = {
    '0':(-1,0),
    '1':(-2,1),
    '2':(-1,1),
    '3':(0,1),
    '4':(-2,2),
    '5':(-1,2),
    '6':(0,2),
    '7':(-2,3),
    '8':(-1,3),
    '9':(0,3),
    'A':(0,0),
    '^':(-1,0),
    '<':(-2,-1),
    'v':(-1,-1),
    '>':(0,-1)
}

def move(t):
    global K, npairs

    npairs[('A',t[0])] += K
    
    for i,j in zip(t,t[1:]):
        npairs[(i,j)] += K

def comp(s,n):
    global K,npairs
    
    pairs=defaultdict(int)
    pairs[('A',s[0])]+=1
    
    for pair in zip(s,s[1:]):
        pairs[pair]+=1
    
    for _ in range(n):
        cx,cy=0,0
        npairs=defaultdict(int)
        for pair in pairs:
            K=pairs[pair]
            
            cx,cy=key_locations[pair[0]]
            gx,gy=key_locations[pair[1]]
            
            x,y=gx-cx,gy-cy

            if x==0 and y==0:
                move('A')
            elif x==0 and y>0:
                move('^'*y+'A')
            elif x==0 and y<0:
                move('v'*-y+'A')
            elif y==0 and x<0:
                move('<'*-x+'A')
            elif y==0 and x>0:
                move('>'*x+'A')
            elif y>0 and x>0 and (cx!=-2 or gy!=0):
                move('^'*y+'>'*x+'A')
            elif y>0 and x>0:
                move('>'*x+'^'*y+'A')
            elif y>0 and x<0 and (cy!=0 or gx!=-2):
                move('<'*-x+'^'*y+'A')
            elif y>0 and x<0:
                move('^'*y+'<'*-x+'A')
            elif y<0 and x>0 and (cx!=-2 or gy!=0):
                move('v'*-y+'>'*x+'A')
            elif y<0 and x>0:
                move('>'*x+'v'*-y+'A')
            elif (cy!=0 or gx!=-2):
                move('<'*-x+'v'*-y+'A')
            else:
                move('v'*-y+'<'*-x+'A')
        pairs=npairs
    return sum(pairs[i] for i in pairs)

print(sum(comp(i,26)*int(i[:-1]) for i in mp))