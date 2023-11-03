import sys
input = sys.stdin.readline

paper = [[0] * 100 for _ in range(100)]
cnt = 0

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for k in range(100):
    cnt += paper[k].count(1)

print(cnt)