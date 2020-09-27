#사분면 고르기
import sys
input = sys.stdin.readline
x = input()
y = input()

if int(x) >0 and int(y) >0:
    print(1)
elif int(x)<0 and int(y)>0:
    print(2)
elif int(x)<0 and int(y)<0:
    print(3)
else:
    print(4)
