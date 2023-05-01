import sys
input = sys.stdin.readline

s1 = input().strip().upper()
s2 = input().strip().upper()
len1 = len(s1)
len2 = len(s2)
mat = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if s1[i-1]==s2[j-1]:
            mat[i][j] = mat[i-1][j-1] + 1
        else:
            mat[i][j] = max(mat[i-1][j], mat[i][j-1])

print(mat[-1][-1])