import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

result = []
for i in range(N, M+1):
  cnt = 0
  if i > 1:
    for j in range(2, i):
      if i % j == 0: # 소수 아닌 것들 모이고
        cnt += 1
        break
    if cnt == 0:
      result.append(i)

if len(result) > 0:
  print(sum(result))
  print(min(result))
else:
  print(-1)