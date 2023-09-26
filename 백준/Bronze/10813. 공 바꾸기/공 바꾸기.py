import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_list = [i for i in range(1, N+1)]

for _ in range(M):
  i, j = map(int, input().split())
  n_list[i-1], n_list[j-1] = n_list[j-1], n_list[i-1]

for i in range(N):
  print(n_list[i], end=' ')
