# 24.03.05

import sys
import math
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

a = math.ceil(W / (M + 1))
b = math.ceil(H / (N + 1))

print(a * b)