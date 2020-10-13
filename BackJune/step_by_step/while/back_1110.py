#더하기 사이클
import sys
input = sys.stdin.readline
first_n = input().rstrip()

#count=0
#N = '0'+N if int(N) < 10 else N
#N_list = list(map(int, N))
#while True:
#    new_N = str(N_list[-1]) + str(sum(N_list)%10)
#    N_list = list(map(int, new_N))
#    if int(N) == int(new_N):
#        print(count+1)
#        break
#    elif int(N) <=0:
#        print(1)
#    else:
#        count +=1

count=1
org_N = int(first_n)
while True:
    one = int(first_n) % 10
    ten = int(int(first_n) / 10)
    res = ten + one
    tmp = int(str(one)+str(res % 10))
    first_n = tmp
    if org_N == tmp:
        break
    else:
        count +=1
print(count)
        

