#한수
def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if i <=99:
            cnt +=1
        else:
            nums = list(map(int, str(i)))
            if nums[0] - nums[1] == nums[1] - nums[2]:
                cnt +=1
    print(cnt)
main()