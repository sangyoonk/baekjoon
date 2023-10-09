import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
  X = list(map(int, input().split()))
  if X[0] == 1:
    stack.append(X[1])
  elif X[0] == 2:
    print(stack.pop() if len(stack) else -1)
  elif X[0] == 3:
    print(len(stack))
  elif X[0] == 4:
    print(0 if len(stack) else 1)
  elif X[0] == 5:
    print(stack[-1] if len(stack) else -1)