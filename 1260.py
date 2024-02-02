# 24.02.03
# N: 정점의 개수
# V: 간선의 개수
# start: 탐색을 시작할 정점의 번호
# graph: 그래프

import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    visited1[start] = True
    print(start, end = " ")
    for i in range(1, N + 1):
        if not visited1[i] and graph[start][i]:
            dfs(i)
            
def bfs(start):
    queue = deque([start])
    visited2[start] = True
    
    while queue:
        x = queue.popleft()
        print(x, end = " ")
        
        for i in range(1, N + 1):
            if not visited2[i] and graph[x][i]:
                queue.append(i)
                visited2[i] = True

N, V, start = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited1 = [False] * (N + 1) # for dfs
visited2 = [False] * (N + 1) # for bfs
for _ in range(V):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
dfs(start)
print()
bfs(start)