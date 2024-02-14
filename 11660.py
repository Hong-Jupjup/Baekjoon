# 24.02.14
# N, M: 표의 크기, 합을 구해야 하는 횟수

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (N + 1)]
for i in range(N):
    graph.append([0] + list(map(int, input().split())))
    
# 가로 누적합
for i in range(N + 1):
    for j in range(1, N + 1):
        graph[i][j] += graph[i][j - 1]

# 세로 누적합
for i in range(1, N + 1):
    for j in range(N + 1):
        graph[i][j] += graph[i - 1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(graph[x2][y2] - graph[x2][y1 - 1] - graph[x1 - 1][y2] + graph[x1 - 1][y1 - 1])
    