# 24.01.08

import sys
input = sys.stdin.readline

while True:
    flag = 0
    a = str(input().strip())
    length = len(a)
    if a == '0':
        break
    
    for i in range(length // 2):
        if a[i] != a[length - i - 1]:
            print("no")
            flag = 1
            break
    
    if flag == 0:
        print("yes")