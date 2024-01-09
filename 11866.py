# 24.01.09
# N: 사람 수
# K: 제거 되는 사람 수

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = list(range(1, N + 1))
idx = 0
result = []

while queue:
    idx += K - 1
    if idx >= len(queue):
        idx %= len(queue)
    result.append(str(queue.pop(idx)))

print("<", ", ".join(result), ">", sep = "")