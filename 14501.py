# 24.03.18
# N: 남은 일 수
# T, P: 시간, 금액

import sys
input = sys.stdin.readline

N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i + 1]
        
    else:
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
        
print(dp[0])