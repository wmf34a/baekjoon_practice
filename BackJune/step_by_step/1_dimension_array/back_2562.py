#최대값
import sys
input = sys.stdin.readline
n_max = 0
cnt = 0
for i in range(1,10):
    n = int(input())
    if n > n_max:
        n_max = n
        cnt = i
print(n_max, cnt,sep='\n')