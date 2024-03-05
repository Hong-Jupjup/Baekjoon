# 24.03.05

import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    
    if a + b <= c or b + c <= a or c + a <= b:
        print("Invalid")
        
    elif a == b and b == c:
        print("Equilateral")
        
    elif a == b or b == c or c == a:
        print("Isosceles")
        
    else:
        print("Scalene")