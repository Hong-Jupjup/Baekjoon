# 24.01.31
# PyPy3
# N, M: 가로, 세로 (3 <= N, M <= 8)
# 0, 1, 2: 빈 칸, 벽, 바이러스
# graph: 그래프 리스트

import sys
from collections import deque
import copy
input = sys.stdin.readline

def bfs():
    queue = deque()
    test_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i, j))
                
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if test_graph[nx][ny] == 0:
                    test_graph[nx][ny] = 2
                    queue.append((nx, ny))
                    
    global result
    count = 0
    for i in range(N):
        for j in range(M):
            if test_graph[i][j] == 0:
                count += 1
    
    result = max(result, count)

def make_wall(count):
    if count == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count + 1)
                graph[i][j] = 0
                
if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    result = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    make_wall(0)
    
    print(result)