# 24.03.07

import sys
input = sys.stdin.readline

mo = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input().strip()
    
    has_mo = 0 # 모음이 있는지 여부
    three = 0 # 모음 3개 혹은 자음 3개 연속 여부
    yeon = 0 # 같은 글자 연속 여부
    accept = 0 # 최종 판단, 0은 False
    
    if password == 'end':
        break
    
    for i in range(len(password)):
        if not has_mo and password[i] in mo:
            has_mo = 1
            
    for i in range(len(password) - 1):
        if password[i] not in ('e', 'o') and password[i] == password[i + 1]:
            yeon = 1
            
    for i in range(len(password) - 2):
        if password[i] in mo and password[i + 1] in mo and password[i + 2] in mo:
            three = 1
            
        if password[i] not in mo and password[i + 1] not in mo and password[i + 2] not in mo:
            three = 1
            
    if has_mo == 0 or yeon == 1 or three == 1:
        print('<' + password + '> is not acceptable.')
        
    else:
        print('<' + password + '> is acceptable.')