#평균
import sys
input = sys.stdin.readline
N = int(input())
M = list(map(int,input().split()))
M_max = max(M)
average = 0
for i in range(N):
    average += (M[i]/M_max*100)/N
print("%.2f" %average)
