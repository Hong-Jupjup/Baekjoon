# 24.03.18
# n, k: 동전 종류, 가치의 합

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
coins.sort()

dp = [0] * (k + 1)
dp[0] = 1

for c in coins:
    for i in range(c, k + 1):
        dp[i] += dp[i - c]
        
print(dp[k])