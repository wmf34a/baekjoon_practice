# 동전 0
import sys
input = sys.stdin.readline

N,total = map(int, input().split())
coin_list = []

for _ in range(N):
    coin = int(input())
    coin_list.append(coin)

cnt = 0
for i in reversed(coin_list):
    if i <= total and total > 0:
        if total // i > 0:
            cnt +=int(total // i)
            total -= i*int(total // i)
print (cnt)
