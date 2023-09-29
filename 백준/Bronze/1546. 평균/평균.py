import sys
input = sys.stdin.readline

n = int(input())

s = list(map(int, input().split()))
print(sum(s)/n/max(s)*100)