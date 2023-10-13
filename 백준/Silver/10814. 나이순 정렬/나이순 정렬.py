import sys
input = sys.stdin.readline

n = int(input())
m = []

for i in range(n):
  age, name = input().split()
  age = int(age)
  m.append((age, name))

m.sort(key = lambda x : x[0])

for i in m:
  print(i[0], i[1])