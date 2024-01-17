# 24.01.17
# N: 도감에 수록되어 있는 포켓몬의 개수
# M: 내가 맞혀야 하는 문제의 개수
# pokemon: 포켓몬 딕셔너리

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}
for i in range(1, N + 1):
    a = input().strip()
    pokemon[i] = a
    pokemon[a] = i

for i in range(M):
    quest = input().strip()
    if quest.isdigit():
        print(pokemon[int(quest)])
    else:
        print(pokemon[quest])