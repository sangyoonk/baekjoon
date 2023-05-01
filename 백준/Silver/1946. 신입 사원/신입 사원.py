import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    a = []
    for j in range(n):
        x, y = map(int, input().split())
        a.append([x,y])
    a.sort()

    L = a[0][1]
    index = 1
    for j in range(1, n):
        if a[j][1] < L:
            L = a[j][1]
            index += 1
    print(index)