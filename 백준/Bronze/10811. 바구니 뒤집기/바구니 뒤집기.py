import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = [i for i in range(1, n+1)] 

for i in range(m):
  a, b = map(int, input().split())
  num[a-1:b] = reversed(num[a-1:b])

print(*num)