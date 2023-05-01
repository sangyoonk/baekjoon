import sys

input = sys.stdin.readline

total = int(input())

for i in range(total):
    num1, num2 = input().split()
    print(int(num1)+int(num2))