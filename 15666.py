# 24.02.05

import sys
from itertools import combinations_with_replacement as cwr
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
result = set()

for i in cwr(array, M):
    result.add(i)
    
result = sorted(result)

for i in result:
    print(*i)