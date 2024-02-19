# 24.02.19

'''
<메모>
        A   C   A   Y   K   P
        0   0   0   0   0   0
C   0   0   1   1   1   1   1
A   0   1   1   2   2   2   2
P   0   1   1   2   2   2   3
C   0   1   2   2   2   2   3
A   0   1   2   3   3   3   3
K   0   1   2   3   3   4   4
'''

import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
len1 = len(str1)
len2 = len(str2)
cache = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i - 1] == str2[j - 1]:
            cache[i][j] = cache[i - 1][j - 1] + 1
        else:
            cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
            
print(cache[-1][-1])