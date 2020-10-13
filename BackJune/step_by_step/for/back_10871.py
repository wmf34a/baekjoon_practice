#x보다 작은 수
import sys
input = sys.stdin.readline
N,X = map(int,input().split())
num = list(map(int,input().split()))
for i in range(N):
    if num[i] < X:
        print(num[i], end=" ")



