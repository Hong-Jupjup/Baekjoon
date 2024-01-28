# 24.01.27
# N: 연산의 개수
# x: 0이 아니면 배열에 x 추가, 0이면 절댓값이 가장 작은 값을 출력하고 배열에서 제거
# abs_heap: 절댓값 힙

import sys
import heapq
input = sys.stdin.readline

N = int(input())
abs_heap = []

for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(abs_heap, (abs(x), x))
    else:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)