# 24.02.20
'''
<메모>
입력: A+B*C-D/E
((A + (B * C)) - (D / E))
(A + BC*) - (D / E)
ABC*+ - (D / E)
ABC*+ - DE/
ABC*+DE/-
'''

import sys
input = sys.stdin.readline

strn = list(input())
stack = []
res = ''

for s in strn:
    if s.isalpha():
        res += s
    
    else:
        if s == '(':
            stack.append(s)
        
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(s)
            
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(s)
            
        elif s == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
            
while stack:
    res += stack.pop()

print(res)