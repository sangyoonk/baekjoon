import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
  m = int(input())
  Q = m // 25
  Q_rest = m % 25
  D = Q_rest // 10
  D_rest = Q_rest % 10
  N = D_rest // 5
  N_rest = D_rest % 5
  P = N_rest // 1
  P_rest = N_rest % 1

  print(Q, D, N, P)