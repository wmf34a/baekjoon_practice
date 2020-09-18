input_num = int(input())

for i in range(1, input_num+1):
    num_list = list(map(int, str(i)))
    result = i + sum(num_list)
    if result == input_num:
        print(i)
        break
    if i == input_num:
        print(0)