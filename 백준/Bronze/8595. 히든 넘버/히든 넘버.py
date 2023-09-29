import sys
input = sys.stdin.readline

n = int(input())
c = input()

num = '1234567890'
hidden_sum = 0
current_num = 0

for i in c:
  if i in num:
    current_num = current_num * 10 + int(i)
  else:
    hidden_sum += current_num
    current_num = 0

hidden_sum += current_num

print(hidden_sum)