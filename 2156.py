# 24.03.16
# n: 포도주 잔의 개수

'''
<메모>
1. 현재 포도주와 이전 포도주를 마시고 전전 포도주는 안 마심 (wine[i] + wine[i - 1] + dp[i - 3])
2. 현재 포도주와 전전 포도주를 마시고 이전 포도주는 안 마심 (wine[i] + dp[i - 2])
3. 현재 포도주는 안 마심 (dp[i - 1])
'''

import sys
input = sys.stdin.readline

n = int(input())
wine = list(int(input()) for _ in range(n))

dp = [0] * n
dp[0] = wine[0]

if n > 1:
    dp[1] = wine[0] + wine[1]
    
if n > 2:
    dp[2] = max(wine[2] + wine[1], wine[2] + wine[0], dp[1])
    
for i in range(3, n):
    dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2], dp[i - 1])
    
print(dp[n - 1])