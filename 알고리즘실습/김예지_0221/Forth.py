test = int(input())

for tc in range(1, test+1):
    forth = input().split()
    stack = []
    flag = 0

    for cal in forth:
        num = []
        if cal == '.':
            if len(stack) > 1:
                print(f'#{tc} error')
                break
            else:
                stack = ''.join(map(str, stack))
                print(f'#{tc} {stack}')
                break
        if cal.isdecimal():
            stack.append(int(cal))
        else:
            if cal == '+':
                for i in range(2):
                    if len(stack) != 0:
                        oper = stack.pop()
                        num.append(oper)
                    else:
                        flag = 1
                        break
                if flag == 0:
                    result = num[1] + num[0]
                    stack.append(result)
                else:
                    break

            elif cal == '-':
                for i in range(2):
                    if len(stack) != 0:
                        oper = stack.pop()
                        num.append(oper)
                    else:
                        flag = 1
                        break
                if flag == 0:
                    result = num[1] - num[0]
                    stack.append(result)
                else:
                    break

            elif cal == '/':
                for i in range(2):
                    if len(stack) != 0:
                        oper = stack.pop()
                        num.append(oper)
                    else:
                        flag = 1
                        break
                if flag == 0:
                    result = num[1] // num[0]
                    stack.append(result)
                else:
                    break

            elif cal == '*':
                for i in range(2):
                    if len(stack) != 0:
                        oper = stack.pop()
                        num.append(oper)
                    else:
                        flag = 1
                        break
                if flag == 0:
                    result = num[1] * num[0]
                    stack.append(result)
                else:
                    break

    if flag:
        print(f'#{tc} error')