def dfs(depth):

  if depth == n:
    print(*visited)
  else:
    for i in range(n):
      if i + 1 in visited: # 방문한적 있으면
        continue # 제외
      visited[depth] = i + 1
      dfs(depth + 1)
      visited[depth] = 0


n = int(input())
visited = [0] * n
dfs(0)