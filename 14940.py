# 24.01.17
# n: 세로의 크기
# m: 가로의 크기
# 0, 1, 2: 갈 수 없는 땅, 갈 수 있는 땅, 목표지점

import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = True
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                
n, m = map(int, input().split())
graph = []
x, y = 0, 0
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x, y = i, j
            break

bfs(x, y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            graph[i][j] = -1
            
for i in graph:
    for j in i:
        print(j, end = ' ')
    print()