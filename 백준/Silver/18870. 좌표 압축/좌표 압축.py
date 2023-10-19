from sys import stdin
input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(set(arr))

dic = {val:idx for idx, val in enumerate(arr2)}

for i in arr:
    print(dic[i], end=' ')