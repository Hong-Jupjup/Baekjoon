# 24.03.19
# pipe: 파이프 괄호 리스트

import sys
input = sys.stdin.readline

pipe = list(input().strip())
stack = []
answer = 0

for i in range(len(pipe)):
    if pipe[i] == '(':
        stack.append('(')
        
    elif pipe[i] == ')':
        if pipe[i - 1] == '(':
            # 레이저
            stack.pop()
            answer += len(stack)
            
        elif pipe[i - 1] == ')':
            # 파이프
            stack.pop()
            answer += 1
            
print(answer)