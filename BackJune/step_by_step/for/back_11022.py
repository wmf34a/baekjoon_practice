#A+B-7
import sys
input = sys.stdin.readline
N = int(input().rstrip())
for i in range(N):
    A,B = map(int, input().split())
    print("Case #{x}: {y} + {z} = {res}".format(x=i+1, y=A,res=A+B))