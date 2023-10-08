n = int(input())
m = int(input())
k = int(input())

h = n + m + k
if h == 180:
  if n == 60 and m == 60 and k == 60:
    print("Equilateral")
  elif n == m or n == k or k == m:
    print("Isosceles")
  elif n != m and n != k and k != m:
    print("Scalene")
else:
  print("Error")