# 24.02.07
# n: 삼각형의 크기
# tri: 삼각형 리스트

import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

dp = deepcopy(tri)

for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0:
            dp[i][0] = dp[i - 1][0] + tri[i][0]
        elif j == len(tri[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + tri[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + tri[i][j]
            
print(max(dp[n - 1]))