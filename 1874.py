# 24.01.11
# n: 수열을 이루는 최대 숫자 (1 ~ n)

import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
find = True
now = 1

for _ in range(n):
    tmp = int(input())
    
    while now <= tmp:
        stack.append(now)
        result.append('+')
        now += 1
        
    if stack[-1] == tmp:
        stack.pop()
        result.append('-')
        
    else:
        find = False
        
if not find:
    print('NO')

else:
    for i in result:
        print(i)