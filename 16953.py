# 24.02.14
# A -> B

import sys
from collections import deque
input = sys.stdin.readline

def cal1(A):
    return 2 * A

def cal2(A):
    return 10 * A + 1

def dfs():
    while queue:
        a, c = queue.popleft()
        
        if a == B:
            print(c)
            return
        
        if cal1(a) <= B:
            queue.append((cal1(a), c + 1))
            
        if cal2(a) <= B:
            queue.append((cal2(a), c + 1))
            
    print(-1)

A, B = map(int, input().split())
queue = deque()
queue.append((A, 1))

dfs()