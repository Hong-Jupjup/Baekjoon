# 24.02.04
# N, M
# arr: 숫자 리스트
# result: 결과 집합 (중복 제거)

import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = set()

for i in permutations(arr, M):
    result.add(i)

result = sorted(result)

for i in result:
    print(*i)