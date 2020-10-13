#최소, 최대
import sys
input = sys.stdin.readline
N = input()

num_list = list(map(int, input().split()))
print(min(num_list), max(num_list), end='')

#num_list = list(map(int, input().split()))
#n_max = num_list[0]
#n_min = num_list[0]
#for i in num_list:
#    if i > n_max:
#        n_max = i
#    if i < n_min:
#        n_min = i
#print(n_min, n_max,end='')