# 24.01.29
# N: 이동하려고 하는 채널 (0 <= N <= 500_000)
# M: 고장난 버튼의 개수 (0 <= M <= 10)
# error: 고장난 버튼 리스트

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

if M == 0:
    error = []
else:
    error = list(map(int, input().split()))    

ans = abs(100 - N)

for i in range(999_999):
    num = str(i)
    
    for j in num:
        if int(j) in error:
            break
    
    else:
        ans = min(ans, abs(N - i) + len(num))
        
print(ans)