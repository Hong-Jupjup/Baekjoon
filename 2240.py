# 24.03.25
# T, W: 자두가 떨어지는 초 수, 자가 움직이고 싶어하는 횟수

import sys
input = sys.stdin.readline

T, W = map(int, input().split())
plums = [0] + list(int(input()) for _ in range(T))
dp = [[0] * (W + 1) for _ in range(T + 1)]

dp[1][0], dp[1][1] = plums[1] % 2, plums[1] // 2

for t in range(2, T + 1):
    for w in range(W + 1):
        if w % 2 == 0:
            j = plums[t] % 2
            
        else:
            j = plums[t] // 2
        
        dp[t][w] = max(dp[t - 1][0:w + 1]) + j
        
print(max(dp[-1]))