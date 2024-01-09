# 24.01.09
# K: 가지고 있는 랜선의 개수
# N: 필요한 랜선의 개수
# lan: 랜선 리스트

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = []
for _ in range(K):
    lan.append(int(input()))

start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    count = 0
    
    for i in lan:
        count += i // mid
    
    if count >= N:
        start = mid + 1
    
    else:
        end = mid - 1
        
print(end)

'''
<후기>
의외로 이분탐색으로 푸는 문제였다.
'''