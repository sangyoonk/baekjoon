import sys
input = sys.stdin.readline

X = input()

if X[:2] == '0x':
  print(int(X, 16))
elif X[0] == '0':
  print(int(X, 8))
else:
  print(int(X))