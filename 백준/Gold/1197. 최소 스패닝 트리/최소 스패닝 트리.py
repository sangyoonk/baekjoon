import sys

input = sys.stdin.readline

# 최소 스패닝 트리
# 유니온 파인드

# 부모 노드 찾기
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])

    return parent[a]

# 트리 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    # 작은 루트 노드를 기준으로 합침
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2]) # 간선들을 가중치 기준으로 정렬시킨다.
parent = [i for i in range(V + 1)]
answer = 0

# 반복문을 통해 간선들의 두 정점을 확인
for s, e, w in graph:
    # 부모 노드가 같지 않다면 스패닝 트리!
    if find(s) != find(e):
        union(s, e) # 두 노드를 합친다.
        answer += w

print(answer)