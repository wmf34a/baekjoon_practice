#두수 비교
A,B = input().split()

A = int(A)
B = int(B)

if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')