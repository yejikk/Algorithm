def solution(n, m, k):
    answer = []
    strN = ['('] * n
    strM = [')'] * m
    total = strN + strM
    temp = [0] * (n+m)

    def comb(no):
        nonlocal n, m, k, temp
        if len(answer) == k:
            return

        if no >= (n+m):
            if sum(temp) == n:
                result = []
                for i in range(n+m):
                    if temp[i]:
                        result.append('(')
                    else:
                        result.append(')')
                answer.append(result)
            return

        temp[no] = 1
        comb(no+1)
        temp[no] = 0
        comb(no+1)

    comb(0)
    print(answer)

    if answer[8] == False:
        print("ok")
    else:
        print("no")
solution(2, 2, 5)