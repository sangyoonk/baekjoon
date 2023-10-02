import sys
input = sys.stdin.readline
m = []

for _ in range(5):
  n = int(input())
  m.append(n)

m.sort()
print(f'{int(sum(m)/5)}')
print(m[2])