t = []

m = int(input())

for i in range(m):
    n = int(input())
    if n == 0:
        t.pop()
    else:
        t.append(n)

print(sum(t))