import sys

input=sys.stdin.readline

n = int(input())
n_list = []

for i in range(n):
    m = int(input())
    n_list.append(m)

n_list.sort()

for i in n_list:
    print(i)