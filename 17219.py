# 24.01.18
# N, M: 저장된 사이트 주소의 수, 비밀번호를 찾으려는 사이트 주소의 수
# dic = (주소, 비밀번호) 딕셔너리

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    site, password = map(str, input().split())
    dic[site] = password
    
for _ in range(M):
    print(dic[input().strip()])