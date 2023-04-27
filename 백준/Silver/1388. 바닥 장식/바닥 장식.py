import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n 세로, m 가로

graph = [input().strip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0

def dfs(x,y): # x 세로, y 가로
    visited[x][y] = True #방문시 체크
    if y+1 < m and graph[x][y] == '-' and graph[x][y+1] == '-': # 오른쪽으로 한 칸씩 이동하면서 체크
        # print(graph[x][y])
        dfs(x, y+1)
    elif x+1 < n and graph[x][y] == '|' and graph[x+1][y] == '|':   # 아래로 한 칸씩 이동하면서 체크
        dfs(x+1, y)

for i in range(n): # row마다 체크
    for j in range(m): # col마다 체크
        if visited[i][j] == False: # 방문 하지 않았다면
            dfs(i,j)
            cnt += 1

print(cnt)