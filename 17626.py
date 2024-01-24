# 24.01.24
# PyPy3
# n: 합이 n이 되도록 하는 제곱수들의 최소 개수 구하기

import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    min_val = 99999
    for j in range(1, int(math.sqrt(i)) + 1):
        min_val = min(min_val, dp[i - j ** 2])
    dp.append(min_val + 1)
    
print(dp[n])