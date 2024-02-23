# 24.02.23
# s: 문자열
# b: 폭발 문자열

import sys
input = sys.stdin.readline

s = input().strip()
b = input().strip()
len_b = len(b)
stack = []

for i in s:
    stack.append(i)
    if b[-1] == stack[-1] and ''.join(stack[-len_b:]) == b:
        del stack[-len_b:]
        
print(''.join(stack) if stack else 'FRULA')