# N: 최대 개수
# K: 최대 무게
# W, V: 각 물건의 무게와 가치
# items: (W, V) 리스트

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = [(0, 0)]
for _ in range(N):
    tmp1, tmp2 = map(int, input().split())
    items.append((tmp1, tmp2))

# DP table
dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = items[i][0]
        value = items[i][1]
        if j < weight: # 가방에 넣을 수 없으면
            dp[i][j] = dp[i - 1][j] # 윗 값 그대로
        else: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

# print(dp)
print(dp[N][K])

'''
무게 가치
6 13
4 8
3 6
5 12

dp table
'''

'''
<후기>
Knapsack을 인지하고 0-1 문제가 아니므로 dp로 풀어야한다고 생각했다.
dp가 익숙치 않아서 dp table을 어떻게 구성해야 하는지 오래 생각했다.
방법 자체는 쉬우므로 다음에 dp 문제가 나오면 어색하지는 않을 것 같다.
'''