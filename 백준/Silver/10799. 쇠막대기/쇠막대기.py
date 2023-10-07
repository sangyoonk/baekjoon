N = list(input())
stack = []
ans = 0

for i in range(len(N)):
  if N[i] == '(':
    stack.append('(')
  
  else:
    if N[i-1] == '(':
      stack.pop()
      ans += len(stack)
    else:
      stack.pop()
      ans += 1

print(ans)