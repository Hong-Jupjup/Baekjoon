# 24.03.04
# N: 구매하려고 하는 카드의 수
# prices: 가격 리스트

import sys
input = sys.stdin.readline

N = int(input())
prices = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + prices[j])
        
print(dp[i])