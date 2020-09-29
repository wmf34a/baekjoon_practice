#구구단
import sys
input = sys.stdin.readline
x = int(input())

for i in range(1,10):
    print("{x} * {i} = {res}".format(x=x, i=i, res=x*i))