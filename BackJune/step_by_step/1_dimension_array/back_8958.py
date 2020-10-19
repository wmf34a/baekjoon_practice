#OX퀴즈
import sys
input = sys.stdin.readline
N = int(input())

ox_list = []
for i in range(N):
    ox_list.append(input().rstrip())

for i in ox_list:
    o_cnt = 0
    score = 0
    for j in i:
        if j == 'O':
            o_cnt +=1
            score += o_cnt
        elif j == 'X':
            score += 0
            o_cnt = 0
    print(score)


