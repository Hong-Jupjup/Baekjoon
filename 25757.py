# 24.03.06
# N, game: 신청한 횟수, 플ㅔ이할 게임의 종류
# players: 플레이어 리스트

import sys
input = sys.stdin.readline

N, game = input().split()
N = int(N)
players = set(input().strip() for _ in range(N))

if game == 'Y':
    answer = len(players) // 1
    
elif game == 'F':
    answer = len(players) // 2
    
elif game == 'O':
    answer = len(players) // 3
    
print(answer)