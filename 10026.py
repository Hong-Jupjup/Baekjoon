# 24.01.24
# N: NxN 그리드
# graph: 그림
# visited: 구역 나누기
# visited2: 적록색맹 구역 나누기
# cnt: 구역 개수
# cnt2: 적록색맹 구역 개수

import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j, cnt, visited):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([(i, j)])
    
    while queue:
        x, y = queue.popleft()
        
        for k in range(4):
            color = graph[x][y]
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = cnt
                    queue.append((nx, ny))

N = int(input())
graph = []
cnt, cnt2 = 0, 0
visited = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
for _ in range(N):
    graph.append(list(input().strip()))
    
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            cnt += 1
            visited[i][j] = cnt
            bfs(i, j, cnt, visited)
            
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
            
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            cnt2 += 1
            visited2[i][j] = cnt2
            bfs(i, j, cnt2, visited2)
            
print(cnt, cnt2)