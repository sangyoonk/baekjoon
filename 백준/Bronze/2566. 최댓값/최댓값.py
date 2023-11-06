import sys
input = sys.stdin.readline

array = [list(map(int, input().split())) for _ in range(9)]
num = -1
x, y = 0, 0

for i in range(9):
    for j in range(9):
        if array[i][j] > num:
            num = array[i][j]
            x = i + 1
            y = j + 1

print(num)
print(x, y)