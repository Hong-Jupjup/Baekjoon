# 24.01.20
# T: 테스트 케이스 수
# k: 연산의 개수
# I n: 정수 n을 Q에 삽입
# D 1: Q에서 최댓값 삭제
# D -1: Q에서 최솟값 삭제

import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    max_heap, min_heap = [], []
    visited = [False] * 1_000_001
    for i in range(k):
        command, number = input().split()
        number = int(number)
        
        if command == 'I':
            heapq.heappush(min_heap, (number, i))
            heapq.heappush(max_heap, (-number, i))
            visited[i] = True
            
        elif command == 'D':
            if number == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                    
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                    
            if number == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                    
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
        
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if len(min_heap) == 0 or len(max_heap) == 0:
        print('EMPTY')
    
    else:
        print(-max_heap[0][0], min_heap[0][0])