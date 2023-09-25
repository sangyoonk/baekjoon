import sys
input = sys.stdin.readline

x = int(input())
n = int(input())
t = 0

for _ in range(n):
  a, b = map(int, input().split())
  t += a * b

if t == x:
  print('Yes')
else:
  print('No')