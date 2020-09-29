#합
#n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline
N = int(input())

result = (N*(N+1))//2
print(result)
#for _ in range(N):
#    A,B = map(int, input().split())
#    print(A + B)