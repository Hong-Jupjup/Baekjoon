# 24.02.03
# N: 크기가 NxN인 도시
# M: 남길 치킨집 개수
# graph: 그래프 리스트
# r, c: r행 c열
# 0, 1, 2: 빈 칸, 집, 치킨집

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
house, chicken = [], []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append((i, j))
        if graph[i][j] == 2:
            chicken.append((i, j))
            
res = 1e9
for ch in combinations(chicken, M):
    tmp = 0
    for hx, hy in house:
        mini = 1e9
        for cx, cy in ch:
            mini = min(mini, abs(hx - cx) + abs(hy - cy))
        tmp += mini
    res = min(res, tmp)
    
print(res)