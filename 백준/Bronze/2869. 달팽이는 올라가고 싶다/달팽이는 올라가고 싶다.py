# 달팽이는 올라가고 싶다 (수학)
import sys

a, b, v = map(int,sys.stdin.readline().split())

if v == a:
    print(1)
else:
    if (v-a) % (a-b):
        print(int(v-a)//(a-b) + 2)
    else:
        print(int(v-a)//(a-b) + 1)