lst = []

for i in range(5):
    a = input()
    lst.append(a)

max_length = max(len(s) for s in lst)

for i in range(max_length):
    for k in lst:
        if i < len(k):
            print(k[i], end='')
print()

