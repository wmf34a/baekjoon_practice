#셀프 넘버
def main():
    num_list = list(range(1,10001))
    del_list = []
    for num in num_list:
        for n in str(num):
            num += int(n)
        if num <= 10000:
            del_list.append(num)
        
    for del_num in set(del_list):
        num_list.remove(del_num)
    for res in num_list:
        print(res)
main()