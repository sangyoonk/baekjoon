import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))

k = n_list + m_list
k.sort()
print(*k)