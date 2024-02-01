# 24.02.01
# N: 국가의 수
# K: 등수를 알고 싶은 국가
# country: 나라 리스트

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
country = []
for i in range(N):
    country.append(list(map(int, input().split())))

country.sort(key = lambda x: (x[1], x[2], x[3]), reverse = True)

idx = [country[i][0] for i in range(N)].index(K)

for i in range(N):
    if country[idx][1:] == country[i][1:]:
        print(i + 1)
        break