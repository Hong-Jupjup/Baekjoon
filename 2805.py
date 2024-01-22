# 24.01.22
# N, M: 나무의 수, 가져갈 나무의 길이
# trees: 나무 길이 리스트

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for tree in trees:
        if tree >= mid:
            cnt += tree - mid
    
    if cnt >= M:
        start = mid + 1
        
    else:
        end = mid - 1
        
print(end)