import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

a = min(n_list)
b = max(n_list)

print(a, b)