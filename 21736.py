# 24.01.20
# N, M: 세로, 가로 길이
# O, X, I, P: 빈 공간, 벽, 도연이, 사람
# start: 시작 좌표
# graph: 지도 그래프

import sys
from collections import deque
input = sys.stdin.readline

# input
N, M = map(int, input().split())
start_x, start_y = 0, 0
graph = []

for i in range(N):
    row = list(input().strip())
    for j in range(M):
        if row[j] == 'I':
            start_x = i
            start_y = j
    graph.append(row)

# bfs
queue = deque([(start_x, start_y)])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False] * M for _ in range(N)]
visited[start_x][start_y] = True
cnt = 0

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny <M and visited[nx][ny] == False and graph[nx][ny] != 'X':
            queue.append((nx, ny))
            visited[nx][ny] = True
            
            if graph[nx][ny] == 'P':
                cnt += 1

if cnt:
    print(cnt)
else:
    print('TT')