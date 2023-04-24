import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)

# 그래프 정보 입력 받기
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs
def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

# 1이라 가정하고 호출
dfs(1)

# 결과 출력
for i in range(2, N+1):
    print(visited[i])
