# 24.01.26
# N: 노드의 개수
# 노드, 왼쪽 자식 노드, 오른쪽 자식 노드
# tree: 트리 딕셔너리

import sys
input = sys.stdin.readline

# 전위 순회: (루트) (왼쪽 자식) (오른쪽 자식)
def preorder(root):
    if root != '.':
        print(root, end = '') # root
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right
        
# 중위 순회: (왼쪽 자식) (루트) (오른쪽 자식)
def inorder(root):
    if root != '.':
        inorder(tree[root][0]) # left
        print(root, end = '') # root
        inorder(tree[root][1]) # right
        
# 후위 순회: (왼쪽 자식) (오른쪽 자식) (루트)
def postorder(root):
    if root != '.':
        postorder(tree[root][0]) # left
        postorder(tree[root][1]) # right
        print(root, end = '') # root
        
if __name__ == '__main__':
    N = int(input())
    tree = {}

    for _ in range(N):
        root, left, right = input().strip().split()
        tree[root] = [left, right]
        
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')