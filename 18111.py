# 24.01.16
# M: 가로
# N: 세로
# B: 가지고 있는 블럭의 개수
# graph: 좌표평면

import sys
input = sys.stdin.readline

idx = 0
answer = sys.maxsize

N, M, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for floor in range(257):
    exceed_block, lack_block = 0, 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > floor:
                exceed_block += graph[i][j] - floor
            else:
                lack_block += floor - graph[i][j]
                
    if exceed_block + B >= lack_block:
        if (exceed_block * 2) + lack_block <= answer:
            answer = (exceed_block * 2) + lack_block
            idx = floor

print(answer, idx)