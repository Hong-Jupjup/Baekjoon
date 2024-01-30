# 24.01.30
# N, M: 세로, 가로 (4 <= N, M <= 500)
# paper: 종이 리스트

import sys
input = sys.stdin.readline

def dfs(x, y, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    
    if idx == 3:
        ans = max(ans, total)
        return
    
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                if idx == 1:
                    visited[nx][ny] = True
                    dfs(x, y, idx + 1, total + paper[nx][ny])
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, idx + 1, total + paper[nx][ny])
                visited[nx][ny] = False

N, M = map(int, input().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
max_val = max(map(max, paper))

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, paper[i][j])
        visited[i][j] = False
        
print(ans)