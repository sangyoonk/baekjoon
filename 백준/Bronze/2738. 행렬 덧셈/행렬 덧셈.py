from sys import stdin
input = stdin.readline
n, m = map(int, input().split())

lst_n = []
lst_m = []

for i in range(n):
    lst_n.append(list(map(int, input().split())))

for i in range(n):
    lst_m.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(lst_n[i][j] + lst_m[i][j], end=' ')
    print()
