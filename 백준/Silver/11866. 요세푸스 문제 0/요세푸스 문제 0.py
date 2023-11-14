from collections import deque

dq = deque()

N, K = map(int, input().split())

for i in range(1, N+1):
    dq.append(i)
print('<',end='')

while dq:
    for i in range(K - 1):
        dq.append(dq[0])
        dq.popleft()
    print(dq.popleft(), end='')
    if dq:
        print(',', end=' ')
print('>')