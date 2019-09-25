def solution(n):
    answer = 0
    temp = [0] * n
    jump = []
    def comb(no, cnt):
        nonlocal n, temp, answer, jump
        if cnt > n:
            return

        if no >= n:
            if cnt == n:
                result = []
                for i in range(n):
                    if temp[i]:
                        result.append(temp[i])
                if result not in jump:
                    jump.append(result)
                    answer += 1
            return

        temp[no] = 1
        comb(no + 1, cnt + temp[no])
        temp[no] = 2
        comb(no + 1, cnt + temp[no])
        temp[no] = 0
        comb(no + 1, cnt)

    comb(0, 0)
    return answer

solution(4)