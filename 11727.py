# 24.01.21
# n: 2xn 직사각형

import sys
input = sys.stdin.readline

'''
<메모>
n = 1: 1
n = 2: 3
n = 3: 1 * 2 + 3 = 5
n = 4: 3 * 2 + 5 = 11
n = k: 2f(k - 2) + f(k - 1)
'''

n = int(input())
dp = [0] * 1001

dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]
    
print(dp[n] % 10007)