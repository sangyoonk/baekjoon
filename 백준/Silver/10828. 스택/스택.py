import sys
stack = []
n = int(sys.stdin.readline())

for i in range(n):
    m = sys.stdin.readline().split()
    
    if m[0] == 'push':
        stack.append(int(m[1]))
    elif m[0] =='top':
        if len(stack) >0:
            print(stack[-1])
        else:
            print(-1)
    elif m[0] == 'size':
        print(len(stack))
    elif m[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif m[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)