import sys

input = sys.stdin.readline

num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)


number = list(map(int,input().split()))

for i in range(num1):
    if number[i] < num2:
        print(number[i])