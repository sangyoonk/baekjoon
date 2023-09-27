import sys
input = sys.stdin.readline

while True:
  n = int(input())

  if n == -1:
    break

  n_list = []
  for i in range(1, n):
    if n%i == 0:
      n_list.append(i)
  if sum(n_list) == n:
    print(f'{n} = {" + ".join(map(str, n_list))}')
  else:
    print(f'{n} is NOT perfect.')
        