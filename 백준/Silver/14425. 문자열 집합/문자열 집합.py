import sys
input = sys.stdin.readline

n, m = map(int, input().split())
set_s = set(input().strip() for _ in range(n))
prime_s = [input().strip() for _ in range(m)]
hash_table = {}

for word in set_s:
    hash_table[word] = 1

count = 0
for word in prime_s:
    if word in hash_table:
        count += 1

print(count)