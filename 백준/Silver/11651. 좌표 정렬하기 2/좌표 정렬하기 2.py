import sys
input = sys.stdin.readline

n = int(input())
m = []

for i in range(n):
  x, y = map(int, input().split())
  m.append([y, x])

k = sorted(m)

for y,x in k:
  print(x,y)