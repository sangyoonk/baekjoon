import sys
input = sys.stdin.readline

N = int(input())
M = []

for i in range(N):
  x = list(map(int, input().split()))
  M.append(x)
M.sort()
  
for j in M:
  print(*j)