#백준 잃어버린 괄호
import sys
input = sys.stdin.readline
str_input = input().rstrip().split('-')
num = [] 
for i in str_input:
    hap = 0
    num_list = i.split('+')
    for j in num_list:
        hap +=int(j)
    num.append(hap)
N = num[0]
for i in range(1, len(num)):
    N -= num[i]
print(N)