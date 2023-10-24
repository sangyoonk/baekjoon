from sys import stdin
input = stdin.readline


while True:
    a, b = map(int, input().split())

    if a == 0 or b == 0:
        break
    

    print(a + b)