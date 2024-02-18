# 24.02.17
# N: 게임 판의 크기

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break
        
        cur = graph[i][j]
        
        if j + cur < N:
            dp[i][j + cur] += dp[i][j]
            
        if i + cur < N:
            dp[i + cur][j] += dp[i][j]