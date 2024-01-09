# 24.01.09
# N: 가지고 있는 카드의 개수
# numbers: 정수 리스트
# M: 판별할 카드의 개수
# cards: 판별할 카드 리스트

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))
count = {}

for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1
        
for card in cards:
    result = count.get(card)
    if result == None:
        print(0, end = " ")
    else:
        print(result, end = " ")
        
'''
<후기>
이중 for문을 사용하면, 시간 초과가 뜬다.
binary search를 사용하거나, dictionary를 사용해서 시간 복잡도를 줄일 수 있다.
'''