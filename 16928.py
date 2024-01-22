# 24.01.22
# 사다리의 수: N
# 뱀의 수: M
# x, y: 사다리 x -> y
# u, v: 뱀 u -> v
# ladder: 사다리 딕셔너리
# snake: 뱀 딕셔너리
# board: 맵
# visited: 방문 여부

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
ladder, snake = dict(), dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

queue = deque([1])
board = [0] * 101
visited = [False] * 101

while queue:
    x = queue.popleft()
    if x == 100:
        print(board[x])
        break
    
    for dice in range(1, 7):
        next_place = x + dice
        if next_place <= 100 and not visited[next_place]:
            if next_place in ladder.keys():
                next_place = ladder[next_place]
            if next_place in snake.keys():
                next_place = snake[next_place]
            if not visited[next_place]:
                visited[next_place] = True
                board[next_place] = board[x] + 1
                queue.append(next_place)