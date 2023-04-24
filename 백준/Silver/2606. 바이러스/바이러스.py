from collections import deque

N = int(input()) # 컴퓨터의 수
M = int(input()) # 컴퓨터에 직접 연결되어있는 쌍의 수

graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0] * (N + 1)

count = 0

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    count = 0
    while q:
        v = q.popleft()
        for i in range(N + 1):
            if not visited[i] and graph[v][i]:
                q.append(i)
                visited[i] = 1
                count += 1
    return count


def dfs(x):
    global count
    visited[x] = 1
    for i in range(N + 1):
        if not visited[i] and graph[x][i]:
            visited[i] = 1
            count += 1
            dfs(i)
    return count

dfs(1)

print(count)
# print(bfs(1))