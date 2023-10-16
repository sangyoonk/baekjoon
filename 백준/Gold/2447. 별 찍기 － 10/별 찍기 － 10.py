import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def append_star(n):
    if n == 1:
        return ['*']
    
    stars = append_star(n//3)
    l = []

    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s+' '*(n//3)+s)
    for s in stars:
        l.append(s*3)
    return l

n = int(input().strip())
print('\n'.join(append_star(n)))