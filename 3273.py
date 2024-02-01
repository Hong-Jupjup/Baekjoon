# 24.02.01
# n: 수열의 크기
# array: 수열 리스트
# x: ai + aj = x
# i1, i2: 더블 포인터
# cnt: 개수

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
x = int(input())

array.sort()
i1, i2 = 0, len(array) - 1
cnt = 0

while i1 < i2:
    if array[i1] + array[i2] == x:
        cnt += 1
        i1 += 1
        i2 -= 1
    
    elif array[i1] + array[i2] < x:
        i1 += 1
        
    elif array[i1] + array[i2] > x:
        i2 -= 1
        
print(cnt)