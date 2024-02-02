# 24.02.02
# n: 도시의 개수 (1 <= n <= 1_000)
# m: 버스의 개수 (1 <= n <= 100_000)
# graph: 버스 리스트
# start, end: 구하고자 하는 구간 출발점의 도시번호, 도착점의 도시번호

import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph, start):
    distances = [int(1e9)] * (n + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        dist, node = heapq.heappop(queue)
        if distances[node] < dist:
            continue
        
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist
            if distance < distances[next_node]:
                distances[next_node] = distance
                parents[next_node] = node
                heapq.heappush(queue, [distance, next_node])
        
    return distances

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
parents = [0] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
start, end = map(int, input().split())

dist_start = dijkstra(graph, start)
print(dist_start[end])

path = []
curr = end
while curr:
    path.append(curr)
    curr = parents[curr]
print(len(path))
for i in path[::-1]:
    print(i, end = " ")