# 24.01.18
# N: 정점의 개수
# graph: 그래프

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
                
for g in graph:
    print(*g)
    
'''
<후기>
Floyd-warshall algorithm
'''