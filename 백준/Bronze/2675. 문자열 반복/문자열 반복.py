n = int(input())
for i in range(n):
    n2, s = input().split()
    for j in s:
        print(int(n2) * j, end="")
    print()