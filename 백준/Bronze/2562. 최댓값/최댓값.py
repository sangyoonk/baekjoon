import sys

input = sys.stdin.readline

lists=[]

for i in range(9):
    lists.append(int(input()))

print(max(lists))
print(lists.index(max(lists))+1)