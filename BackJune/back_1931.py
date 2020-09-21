N = int(input())
a=1
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))


print(arr)
