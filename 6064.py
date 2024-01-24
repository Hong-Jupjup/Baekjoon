# 24.01.24
# T: 테스트 케이스의 개수
# M, N, x, y: <M, N>는 카잉 달력의 마지막 해, <x, y>가 몇 번째 해인지 출력

'''
<메모>
M, N = 10, 12 이면
<1, 1> -> <2, 2> -> ... -> <10, 10> -> <1, 11> -> <2, 12> -> <3, 1> -> ...
'''

import sys
input = sys.stdin.readline

def find_year(M, N, x, y):
    max_year = M * N
    while x <= max_year and (x - 1) % N + 1 != y:
        x += M

    return x if x <= max_year else -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    result = find_year(M, N, x, y)
    print(result)