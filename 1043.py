# 24.02.06
# N, M: 사람의 수, 파티의 수
# truth: 사실을 아는 사람의 수
# party: 파티 참가하는 사람 리스트

# 입력 받기
N, M = map(int, input().split())
truth = set(input().split()[1:])
party = []
for _ in range(M):
    party.append(set(input().split()[1:]))
   
# 알고리즘
for _ in range(M):
    for p in party:
        if p & truth:
            truth = truth.union(p)
            
cnt = 0
for p in party:
    if p & truth:
        continue
    cnt += 1

print(cnt)