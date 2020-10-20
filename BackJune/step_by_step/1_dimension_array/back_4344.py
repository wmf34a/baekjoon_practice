#평균은 넘겠지
import sys
input = sys.stdin.readline
N = int(input())

score_list = []
for i in range(N):
    score_list = list(map(int, input().split(' ')))
    avg = sum(score_list[1:]) / score_list[0]
    cnt = 0
    for j in score_list[1:]:
        if avg < j:
            cnt += 1
    res = cnt/score_list[0] * 100
    print("%.3f"%res+'%')


