# while A+B-4
import sys
input = sys.stdin.readline
while True:
    try:
        A, B = map(int,input().split())
        print(A+B)
    except:
        break