num1, num2 = input().split()

s1 = int(num1[::-1])
s2 = int(num2[::-1])

if s1 > s2:
    print(s1)
else:
    print(s2)