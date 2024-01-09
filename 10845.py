# 24.01.09
# N: 명령의 수
# push X: 정수 X를 큐에 넣는 연산
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력, 정수가 없다면 -1 출력
# size: 큐에 들어있는 정수의 개수 출력
# empty: 큐가 비어있으면 1, 아니면 0 출력
# front: 큐의 가장 앞에 있는 정수 출력, 정수가 없다면 -1 출력
# back: 큐의 가장 뒤에 있는 정수 출력, 정수가 없다면 -1 출력

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
    
    if do == "push":
        queue.append(number)
    
    if do == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
        
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