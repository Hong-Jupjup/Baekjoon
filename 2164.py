# 24.01.08

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a = deque()
for i in range(1, N + 1):
    a.append(str(i))
    
while len(a) > 1:
    a.popleft()
    tmp = a.popleft()
    a.append(tmp)

print(a[0])