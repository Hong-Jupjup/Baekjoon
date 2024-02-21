# 24.02.21
# T: 테스트 케이스의 개수
# N: 트리를 구성하는 노드의 수
# A, B: A가 B의 부모
# a, b: 가장 가까운 공통 조상을 구할 두 노드

import sys
input = sys.stdin.readline

def parent(a):
    p = []
    p.append(a)
    
    for _ in range(N):
        if tree[a] == []:
            break
        else:
            p.append(tree[a])
            
        a = tree[a]
        
    return p

T = int(input())
for _ in range(T):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    a_par, b_par = [], []
    
    for _ in range(N - 1):
        A, B = map(int, input().split())
        tree[B] = A
        
    a, b = map(int, input().split())
    a_par = parent(a)
    b_par = parent(b)
    common = [x for x in a_par if x in b_par]
    
    print(common[0])