import sys
input = sys.stdin.readline

total = [i for i in range(1, 31)]

for i in range(28):
  n = int(input())
  total.remove(n)

print(min(total))
print(max(total))
