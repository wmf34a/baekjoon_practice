import sys
input = sys.stdin.readline

A = input().rstrip()
A_list = list(A)
B = input()
for i in range(len(A_list)-1,-1,-1):
    print(int(B[i])*int(A))
print(int(A)*int(B))

