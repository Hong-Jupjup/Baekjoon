# 24.01.24
# M, N, H: 상자의 가로 칸 수, 상자의 세로 칸 수, 상자의 수
# 1, 0, -1: 익은 토마토, 익지 않은 토마토, 들어있지 않은 칸
# graph: 토마토 개수
# visited: 방문 여부
# result: 토마토가 다 익을 때까지 걸리는 일 수

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
    dx, dy, dz = [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1], [-1, 1, 0, 0, 0, 0]

    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if graph[nx][ny][nz] == 0 and not visited[nx][ny][nz]:
                    visited[nx][ny][nz] = True
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    queue.append((nx, ny, nz))
    

M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        graph[i].append(list(map(int, input().split())))

queue = deque()
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
result = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1 and not visited[i][j][k]:
                queue.append((i, j, k))
                visited[i][j][k] = True

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        result = max(result, max(j))

print(result - 1)

'''
<후기>
bfs 문제지만 graph가 3중 list인 문제.
bfs 자체를 구현하는 건 문제되지 않았지만, 토마토 전체를 확인하는 게 순간 헷갈렸다.
'''