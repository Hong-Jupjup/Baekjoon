# 24.02.13
# N: 도시의 개수
# M: 버스의 개수
# bus: 버스 정보
# s, e, c: s -> e, c는 비용
# s_city, e_city: 출발 도시, 도착 도시

import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if distance[now] < dist:
            continue
        
        for i in bus[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    INF = int(1e9)
    
    bus = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    
    for _ in range(M):
        s, e, c = map(int, input().split())
        bus[s].append((e, c))
        
    s_city, e_city = map(int, input().split())
             
    dijkstra(s_city)
    
    print(distance[e_city])