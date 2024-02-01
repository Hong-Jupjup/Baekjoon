# 24.02.01
# N: 집의 수 (2 <= N <= 1_000)
# RGB: 비용 리스트
# 1번 집의 색은 2번 집의 색과 같지 않아야 함
# N번 집의 색은 N - 1번 집의 색과 같지 않아야 함
# i번 집의 색은 i - 1번, i + 1번 집의 색과 같지 않아야 함

import sys
input = sys.stdin.readline

N = int(input())
RGB = []
for _ in range(N):
    RGB.append(list(map(int, input().split())))

for i in range(1, N):
    # R
    RGB[i][0] = min(RGB[i - 1][1], RGB[i - 1][2]) + RGB[i][0]
    
    # G
    RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]
    
    # B
    RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]
    
print(min(RGB[N - 1]))