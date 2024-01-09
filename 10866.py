# 24.01.09
# N: 명령의 개수
# push_front X: 정수 X를 덱의 앞에 삽입
# push_back X: 정수 X를 덱의 뒤에 삽입
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력, 없으면 -1
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력, 없으면 -1
# size: 덱에 들이있는 정수의 개수 출력
# empty: 덱이 비어있으면 1, 아니면 0 출력
# front: 덱의 가장 앞에 있는 수 출력, 없으면 -1
# back: 덱의 가장 뒤에 있는 수 출력, 없으면 -1

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

for i in range(N):
    command = input()
    if ' ' in command:
        do, number = command.split()
        number = int(number)
    else:
        do = command.strip()
    
    if do == "push_front":
        queue.appendleft(number)
    
    if do == "push_back":
        queue.append(number)
        
    if do == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
            
    if do == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
            
    if do == "size":
        print(len(queue))
        
    if do == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
            
    if do == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            
    if do == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])