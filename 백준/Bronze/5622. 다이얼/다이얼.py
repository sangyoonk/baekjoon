import sys
input = sys.stdin.readline

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alpha = input()
time = 0

for i in alpha:
  for j in dial:
    if i in j:
      time += dial.index(j) + 3

print(time)