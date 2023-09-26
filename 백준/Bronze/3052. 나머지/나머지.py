import sys
input = sys.stdin.readline

n_list = []
for i in range(10):
  n = int(input())
  t = n % 42
  n_list.append(t)

s = set(n_list)
print(len(s))
