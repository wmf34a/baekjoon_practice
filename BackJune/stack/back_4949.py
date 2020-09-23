while True:
    str_input = input()
    if str_input == '.':
        break
    stack_list=[]
    chk = True

    for i in str_input:
        if i == "(" or i == "[":
            stack_list.append(i)
        elif i == ")":
            if stack_list:
                if stack_list.pop() == "(":
                    chk = True
                else:
                    chk = False
                    break
            else:
                chk = False
                break

        elif i == "]":
            if stack_list:
                if stack_list.pop() == "[":
                    chk = True
                else:
                    chk = False
                    break
            else:
                chk = False
                break

    if chk and not stack_list:
        print("yes")
    else:
        print("no")








