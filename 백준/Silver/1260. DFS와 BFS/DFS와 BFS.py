# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
# 그래프 이론과 DFS, BFS를 알고 있다는 전제에 문제 풀이를 해야한다.
# DFS는 재귀, BFS는 큐로 구현하는게 일반적이다.

import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_1 = [False] * (N + 1) # dfs의 방문 기록
visited_2 = [False] * (N + 1) # bfs의 방문 기록

def bfs(V):
    q = deque([V]) # pop 메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용한다
    visited_2[V] = True # 해당 V 값을 방문처리
    while q: # q가 비어있을때까지 반복
        V = q.popleft() # 큐에 있는 첫번쨰 값을 꺼낸다.
        print(V, end=' ') # 해당 값 출력
        for i in range(1, N + 1): # 1부터 N까지 반복문
            if not visited_2[i] and graph[V][i]: # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i) # 그 i 값을 처리
                visited_2[i] = True # i 값을 방문처리

def dfs(V):
    visited_1[V] = True # 해당 V값 방문처리
    print(V, end=' ')
    for i in range(1, N + 1):
        if not visited_1[i] and graph[V][i]: # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i) # 해당 i 값으로 dfs를 돌게 된다 (깊이 더 탐색)

dfs(V)
print()
bfs(V)