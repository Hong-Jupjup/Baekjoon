# 24.02.18
# N, M: NxM 행렬
#0, 1: 이동할 수 있는 곳, 이동할 수 없는 벽이 있는 곳

import sys
from collections import deque
input = sys.stdin.readline

def bfs():   
    queue = deque()
    queue.append((0, 0, 0))
    
    while queue:
        x, y, z = queue.popleft()
        
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
                
            if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
                
    return -1

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

print(bfs())

'''
<후기>
처음에는 다른 bfs 문제처럼 visited를 2중 배열로 나타내고,
2중 for문을 사용하여 벽을 하나씩 없애며 최소값을 구하려고 했다.
답은 맞았으나, 시간초과가 떴다.
시간초과가 뜬다는 것은, bfs를 여러 번 호출하면 안 된다는 뜻.
그래서 3중 배열을 사용하여 가장 마지막 인자를 이미 허물어본 벽인지 아닌지를 했다.
visited[x][y][z]라고 되어 있으면, z는 허문 여부. (0이면 아직 벽 허물지 않음, 1이면 허물어 봄.)
진짜 창의적인 방법이라고 생각한다.
코드도 훨씬 간단해지고, 시간 단축도 잘 된 듯 하다.
벽을 최대 n번까지 허물 수 있다고 조건이 바뀌어도, 이렇게 하면 될 것 같다.
'''