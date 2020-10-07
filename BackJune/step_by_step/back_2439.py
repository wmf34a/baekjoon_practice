#별찍기-2
import sys
input = sys.stdin.readline
N = int(input())

for i in range(1,N+1):
    for j in range(N-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    print()

#    *
#   **
#  ***
# ****
#*****