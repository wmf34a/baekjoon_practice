#나머지
import sys
input = sys.stdin.readline
num_list = []
for _ in range(10):
    num_list.append(int(input())%42)
print(len(set(num_list)))
