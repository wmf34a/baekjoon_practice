#숫자의 개수
import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

res = list(str(A*B*C))

for i in range(0,10):
    print(res.count(str(i)))

