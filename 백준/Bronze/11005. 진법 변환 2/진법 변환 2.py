import sys
input = sys.stdin.readline

N, B = map(int, input().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ''

while N != 0:
  answer += str(arr[N%B])
  N = N // B

print(answer[::-1])