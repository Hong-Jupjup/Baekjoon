# 24.01.19
# T: 테스트 케이스 개수

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    queue = deque()
    queue.append((A, ""))
    visited = [False] * 10000
    
    while queue:
        num, path = queue.popleft()
        visited[num] = True
        if num == B:
            print(path)
            break
        
        # D
        num2 = (2 * num) % 10000
        if not visited[num2]:
            queue.append((num2, path + "D"))
            visited[num2] = True
            
        # S
        num2 = (num - 1) % 10000
        if not visited[num2]:
            queue.append((num2, path + "S"))
            visited[num2] = True
            
        # L
        num2 = (10 * num + (num // 1000)) % 10000
        if not visited[num2]:
            queue.append((num2, path + "L"))
            visited[num2] = True
            
        # R
        num2 = (num // 10 + (num % 10) * 1000) % 10000
        if not visited[num2]:
            queue.append((num2, path + "R"))
            visited[num2] = True