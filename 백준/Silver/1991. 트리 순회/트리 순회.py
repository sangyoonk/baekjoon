import sys

N = int(sys.stdin.readline().strip())
tree = {}

# { A : [B, C] } 이런식으로
# 트리 순회는 재귀 함수로 진행 할 수 있다.
# preorder는 root->left->right 순으로,
# inorder는 left->root->right 순으로,
# postorder는 left->right->root 순으로 출력하도록 하면 된다.
# root가 '.'이 아닐때만 수행하고, root는 출력 left는 다시 함수에 넣어 실행시키는 것이 큰 틀이다.
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
 
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')