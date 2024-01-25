# 24.01.25
# N, M: 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 (오름차순)

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
result = combinations(range(1, N + 1), M)
for i in result:
    print(*i)