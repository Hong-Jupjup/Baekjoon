# 24.01.28
# 1부터 N까지 자연수 중에서 M개를 고른 수열

import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())

result = combinations_with_replacement(range(1, N + 1), M)
for i in result:
    print(*i)