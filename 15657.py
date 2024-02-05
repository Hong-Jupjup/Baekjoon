# 24.02.05

import sys
from itertools import combinations_with_replacement as cwr
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

for i in cwr(array, M):
    print(*i)