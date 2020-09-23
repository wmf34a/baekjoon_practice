import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))
time_sort = sorted(time)

total_time = 0
for i in range(len(time_sort)):
    for j in range(i+1):
        total_time += time_sort[j]
print(total_time)