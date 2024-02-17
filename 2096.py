# 24.02.17
# N: N개의 줄

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
    
max_dp = arr
min_dp = arr

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    max_dp = [a + max(max_dp[0], max_dp[1]), b + max(max_dp), c + max(max_dp[1], max_dp[2])]
    min_dp = [a + min(min_dp[0], min_dp[1]), b + min(min_dp), c + min(min_dp[1], min_dp[2])]
    
print(max(max_dp), min(min_dp))