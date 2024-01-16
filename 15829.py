# 24.01.16
# L: 문자열의 길이
# word: 문자열
# length: 문자열의 길이
# alphabet: 알파벳 딕셔너리

import sys
input = sys.stdin.readline

L = int(input())
word = input().strip()
length = len(word)
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
            'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
            'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
            'z': 26}
result = 0

for i in range(length):
    result += alphabet[word[i]] * (31 ** i)
    
result %= 1234567891

print(result)