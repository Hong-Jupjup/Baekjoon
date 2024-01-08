# 24.01.08
# N: 정수의 개수
# items: 정수 리스트

import sys
import heapq
input = sys.stdin.readline

'''
N = int(input())
items = []
for i in range(N):
    items.append(int(input()))
    items.sort()
    if i % 2 == 0: # i가 짝수: item이 홀수 개
        print(items[i // 2])
    else: # i가 홀수: item이 짝수 개
        print(min(items[i // 2], items[i // 2 + 1]))
'''

N = int(input())
max_heap, min_heap = [], []

for i in range(N):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
        
    if len(max_heap) >= 1 and len(min_heap) >= 1 and max_heap[0] * -1 > min_heap[0]:
        max_value = heapq.heappop(max_heap) * -1
        min_value = heapq.heappop(min_heap)
        
        heapq.heappush(max_heap, min_value * -1)
        heapq.heappush(min_heap, max_value)
        
    print(max_heap[0] * -1)
        
'''
<후기>
Brute-force는 당연하게도 시간 초과가 뜬다.
가운데 값을 찾아야 하므로 heapq를 사용하면 될 것이라 생각했다.

두 개의 heap을 두고, 왼쪽은 max_heap, 오른쪽은 min_heap으로 설정한다.
heapq를 사용하면 min_heap이 기본값이므로 음수로 바꿔서 삽입한다.

양쪽의 heap의 개수가 같으면 왼쪽 heap에 삽입하고, (음수로)
다르면 오른쪽 heap에 삽입한다.

삽입 시,
양쪽 heap에 요소가 존재하고,
왼쪽 heap의 첫 번째 요소의 음수 값이 오른쪽 heap의 첫 번째 요소보다 크면,
서로 바꿔준다.
'''