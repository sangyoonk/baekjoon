import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip()))) 

def bfs(x, y):
    q=deque()
    q.append((x, y))
    cnt = 1

    graph[x][y] = 0  #탐색중인 위치 0으로 바꿔 다시 방문하지 않도록

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

count = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            r = bfs(i,j)
            count.append(r)

# count = [bfs(i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]
# 참고 많이 했습니다.
count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])
