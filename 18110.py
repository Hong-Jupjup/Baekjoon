# 24.01.13
# n: 난이도 의견의 개수
# del_n: 위 아래로 삭제되는 의견의 개수
# input_list: 입력되는 의견 리스트
# op_list: 절사 후 의견 리스트

import sys
input = sys.stdin.readline

def my_round(a):
    if a - int(a) >= 0.5:
        return int(a) + 1
    
    else:
        return int(a)

n = int(input())
del_n = my_round(n * 0.15)
input_list = []
result = 0

if n == 0:
    print(result)

else:
    for _ in range(n):
        input_list.append(int(input()))
    input_list.sort()
    
    if del_n > 0:
        result = my_round(sum(input_list[del_n:-del_n]) / len(input_list[del_n:-del_n]))

    else:
        result = my_round(sum(input_list) / len(input_list))
    
    print(result)