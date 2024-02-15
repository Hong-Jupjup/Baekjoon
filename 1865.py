# 24.02.15
# TC: 테스트 케이스의 개수
# N, M, W: 지점의 수, 도로의 개수, 웜홀의 개수
# S, E, T: 연결된 지점의 번호, 걸리는 시간 / 웜홀 시작 지점, 도착 지점, 줄어드는 시간
# road: 도로
# worm: 웜홀

import sys
input = sys.stdin.readline

def bf():
    for i in range(N):
        for j in range(len(road)):
            cur, next, cost = road[j]
            if distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == N - 1:
                    return True
    
    return False

if __name__ == "__main__":
    TC = int(input())
    for _ in range(TC):
        N, M, W = map(int, input().split())
        road = []
        distance = [1e9] * (N + 1)
        for i in range(M + W):
            S, E, T = map(int, input().split())
            if i >= M:
                T = -T
            else:
                road.append((E, S, T))
                
            road.append((S, E, T))
            
        if bf():
            print("YES")
        else:
            print("NO")