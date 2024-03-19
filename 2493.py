# 24.03.19
# N: 탑의 수
# towers: 탑 높이 리스트

import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > towers[i]:
            answer.append(stack[-1][0] + 1)
            break
        
        else:
            stack.pop()
            
    if not stack:
        answer.append(0)
        
    stack.append([i, towers[i]])
    
print(*answer)