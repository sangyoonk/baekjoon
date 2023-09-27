# 소수 찾기 (수학)

case = int(input())

s = list(map(int, input().split()))
result = 0

for i in s:
    count = 0
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
    if count == 1:
        result +=1

print(result)