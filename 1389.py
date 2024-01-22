# 24.01.22
# N, M: 유저의 수, 친구 관계의 수
# friends: 친구 관계 그래프
'''
<메모>
1-3 1-4 2-3 3-4 4-5
  1 2 3 4 5
1 0   1 1
2   0 1
3 1 1 0 1
4 1 0 1 0 1
5 0 0 0 1 0
'''

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        x = queue.popleft()
        
        for i in friends[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)

N, M = map(int, input().split())
friends = [[] for _ in range(N + 1)]
result = []
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    bfs(i)
    result.append(sum(visited))
    
print(result.index(min(result)) + 1)