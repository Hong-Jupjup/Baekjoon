# 24.03.18

'''
<메모>
N = 1: 1
N = 2: 00 11
N = 3: 001 100 111
N = 4: 0000 0011 1001 1100 1111
N = 5: 00001 00100 10000 00111 10011 11001 11100 11111
'''

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
dp[1] = 1

if N > 1:
    dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    
print(dp[N])