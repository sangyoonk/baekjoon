import sys
input = sys.stdin.readline

n = int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

# 끝나는 시간을 기준으로 해야지만 다음 회의시간을 맞출 수 있다.
time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장수
count = 0 # 회의 개수를 저장할 변수

for i,j in time:
    if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을 경우
        count += 1
        last = j

print(count)