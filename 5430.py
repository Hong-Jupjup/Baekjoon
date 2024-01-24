# 24.01.24
# T: 테스트 케이스의 개수
# p: 수행할 함수 리스트
# n: 배열에 들어있는 수의 개수
# arr: 배열 리스트

import sys
from collections import deque
input = sys.stdin.readline

def f(p, arr):
    flag = 1 # 1은 정방향, -1은 역방향
    result = ''
    # 함수 적용
    for program in p:
        if program == 'R':
            flag = -flag
        if program == 'D':
            if len(arr) == 0:
                print('error')
                return
            
            if flag == 1:
                arr.popleft()
            elif flag == -1:
                arr.pop()
    
    # 출력
    if flag == 1:
        print('[' + ','.join(arr) + ']')
    elif flag == -1:
        arr.reverse()
        print('[' + ','.join(arr) + ']')

T = int(input())
for _ in range(T):
    p = list(input().strip())
    n = int(input())
    arr = input()
    arr = arr[1:len(arr) - 2]
    
    if n != 0:
        arr = list(arr.strip().split(','))
        
    else:
        arr = []
        
    arr = deque(arr)
    f(p, arr)