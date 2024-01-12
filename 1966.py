# 24.01.12
# T: 테스트케이스 수
# N: 문서의 개수
# M: 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지 나타내는 정수 (맨 왼쪽은 0번째)
# priority: N개 문서의 중요도 (1 ~ 9, 중복 가능)

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    priority = deque(priority)
    count = 0
    
    while 1:
        best = max(priority)
        front = priority.popleft()
        M -= 1
        
        if best == front:
            count += 1
            if M < 0:
                print(count)
                break
        
        else:
            priority.append(front)
            if M < 0:
                M = len(priority) - 1