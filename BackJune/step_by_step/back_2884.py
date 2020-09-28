#알람시계
import sys
input = sys.stdin.readline
H, M = input().split()

time_H = int(H)
time_M = int(M) -45

if time_M < 0:
    if time_H == 0:
        time_H = 24

    time_H = time_H-1
    time_M = 60+time_M

print (time_H, time_M)

