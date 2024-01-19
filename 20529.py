# 24.01.19
# T: 테스트 케이스의 수
# N: 학생의 수
# mbits: mbti 리스트

import sys
from itertools import combinations
input = sys.stdin.readline

def mbti_dist(a, b):
    dist = 0
    for i, j in zip(a, b):
        if i != j:
            dist += 1
    return dist

T = int(input())
for _ in range(T):
    N = int(input())
    mbtis = list(map(str, input().split()))
    
    if N > 32:
        print(0)
        
    else:
        res = 100
        case = combinations(mbtis, 3)
        for a, b, c in case:
            dist = 0
            dist += mbti_dist(a, b)
            dist += mbti_dist(b, c)
            dist += mbti_dist(c, a)
            
            res = min(res, dist)
        print(res)
        
'''
<후기>
Brute-force를 쓰는데, 케이스 수가 많아지면 시간 초과가 날 수 밖에 없다.
따라서 비둘기 집의 원리를 사용한다.
비둘기 집의 원리:
    비둘기가 n + 1마리 있고, 집이 n개 있으면 최소 한 비둘기 집에는 비둘기가 두 마리 이상 들어 있다.
MBTI 적용:
    MBTI는 16개이므로, 사람 수가 33명 이상이면 최소 거리는 무조건 0이다.
'''