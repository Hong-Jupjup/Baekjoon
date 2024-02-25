# 24.02.25
# N: N자리 이친수의 개수

'''
<메모>
N = 1: 1
N = 2: 10
N = 3: 100, 101
N = 4: 1000, 1001, 1010
N = 5: 10000, 10001, 10010, 10100, 10101
N = 6: 2 + 1 + 2 + 2 + 1 = 8
피보나치
'''

import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 1]

if N == 1:
    print(1)

else:
    for i in range(2, N + 1):
        dp.append(dp[-2] + dp[-1])
    
    print(dp[N])