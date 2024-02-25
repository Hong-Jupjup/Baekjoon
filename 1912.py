# 24.02.25
# n: 수열 요소의 개수
# arr: 수열

'''
<메모>
10  -4  3   1   5   6   -35 12  21  -1
10
10  10
10  10  10
            10
                10
                    15
                            15
                                33

'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])
    
print(max(dp))