# 24.01.17
# N: 정점의 개수
# M: 간선의 개수

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
count = 0
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1
        
print(count)