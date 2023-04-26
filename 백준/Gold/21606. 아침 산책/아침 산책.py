import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n = int(input())
inside = '0' + input()

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
total = 0

for _ in range(n-1):
    a ,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    if inside[a] == '1' and inside[b] == '1':
        total += 2

def dfs(start):
    visited[start] = True
    inside_count = 0
    for v in graph[start]:
        if inside[v] == '1':
            inside_count += 1

        elif not visited[v] and inside[i] == '0':
            inside_count += dfs(v)
    return inside_count

for i in range(1, n+1):
    if inside[i] == '0' and not visited[i]:
        result = dfs(i)
        total += (result) * (result-1)

print(total)