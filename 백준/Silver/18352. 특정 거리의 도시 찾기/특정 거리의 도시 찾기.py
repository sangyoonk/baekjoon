import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # [[],[2,3],[3,4],[],[]]

visited = [0] * (n+1) 
visited[x] = 1

q=deque()
q.append(x)

while q:
    now = q.popleft()
    for next in graph[now]:
        if not visited[next]:
            visited[next] = visited[now] + 1
            q.append(next)

result = []
for i in range(1, n+1):
    if visited[i] - 1 == k:
        result.append(i)

if result:
    for r in result:
        print(r)
else:
    print(-1)
