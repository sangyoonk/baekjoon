import sys
from collections import deque
input = sys.stdin.readline

# 문제의 point는 모두 도로의 거리가 1이다. 모든 엣지가 1로 동일할 때는 BFS를 이용하여 최단 거리를 찾을 수 있다. 
# 특정한 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 연산 후에, 각 최단거리를 하나씩 확인하며 그 값이 K인 경우에 해당 도시의 번호를 오름차순으로 출력하면 된다.


# N 노드의 수, M 엣지의 수, K 거리정보, X 출발도시 번호
N, M, K, X = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N+1)]

# 엣지 정보 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # [[],[2,3],[3,4],[],[]]

# 모든 도시에 대한 최단 거리 초기화
visited = [-1] * (N+1) # 방문 하지 않는 도시 -1
visited[X] = 0 # 출발 도시 (X) = 0으로 설정

# BFS 알고리즘 수행
q = deque([X])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if visited[next_node] == -1:
            visited[next_node] = visited[now] + 1
            q.append(next_node)

# 결과 출력
result = []
for i in range(1, N+1):
    if visited[i] == K:
        result.append(i)

if result:
    for r in result:
        print(r)
else:
    print(-1)