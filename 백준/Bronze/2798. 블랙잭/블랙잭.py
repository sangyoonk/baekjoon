import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
result = 0

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      if num_list[i] + num_list[j] + num_list[k] > m:
        continue
      else:
        result = max(result, num_list[i] + num_list[j] + num_list[k])

print(result)
