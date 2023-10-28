from sys import stdin
input = stdin.readline

x = []
y = []

for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in x:
    if x.count(i) == 1:
        uni_x = i

for j in y:
    if y.count(j) == 1:
        uni_y = j

print(uni_x, uni_y)