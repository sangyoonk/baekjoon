'''
이 문제는 미로 탈출하는 것을 구현하는 문제인데요, 물과 고슴도치가 움직입니다.
고슴도치는 물이 찰 예정인 지역으로는 이동할 수 없고, 물은 돌이 있는 지역으로는 이동할 수 없습니다.
고슴도치는 물이 찰 예정인 지역을 피해서 비버의 굴로 이동해야 합니다. 즉, 최소한의 시간 내에 비버의 굴로 이동해야 합니다.

이 문제를 풀기 위해서는 BFS(Breadth-First Search) 알고리즘을 사용하면 됩니다. 물과 고슴도치의 이동을 따로 구현하고, BFS를 이용해 최단 시간을 구하면 됩니다.
시작점부터 BFS를 수행하며, 각 칸까지 도달하는 최소 시간을 구합니다. 이때, 물이 먼저 움직여야 하므로 물을 먼저 큐에 넣어주고, 그 다음 고슴도치를 큐에 넣어줍니다.
'''

import sys
from collections import deque
R, C = map(int, input().split())
map = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

visited = [[-1] * C for _ in range(R)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q = deque()

for y in range(R):
    for x in range(C):
        if map[y][x] == '*':  # 물 좌표를 앞에 추가
            q.appendleft((y, x))
        elif map[y][x] == 'S':  # 고슴이 좌표 추가
            q.append((y, x))
            visited[y][x] = 0  # 출발점에 시간 0 저장

while q:
    y, x = q.popleft()
    cur = map[y][x]  # 현재 위치
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]  # 다음에 갈 좌표

        if ny < 0 or ny >= R or nx < 0 or nx >= C:  # 범위 밖이면 무시
            continue
        if visited[ny][nx] != -1:  # 이미 방문한 곳 무시
            continue
        if map[ny][nx] == "*":  # 물 무시
            continue
        if map[ny][nx] == "X":  # 돌 무시
            continue
        if cur == "*" and map[ny][nx] == "D":  # 물이 비버네 가려면 무시
            continue

        if cur == "S":
            if map[ny][nx] == "D":  # 고슴이가 가려는 위치가 비버네면 도착
                print(visited[y][x] + 1)
                break
            visited[ny][nx] = visited[y][x] + 1  # 비버네가 아니면 도착 시간 기록

        map[ny][nx] = cur  # 다음 좌표를 고슴이 or 물로 변경
        q.append((ny, nx))  # 다음 탐색 위치 추가
    else:
        continue
    break
else:
    print("KAKTUS")