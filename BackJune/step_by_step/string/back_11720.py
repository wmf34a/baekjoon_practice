#숫자의 합
import sys
input = sys.stdin.readline
N = int(input())
M = input().rstrip()

if N == 1 :
    print(N)
else:
    print(sum(map(int, list(M))))
