def solution(numbers, target):
    answer = 0

    def comb(no, nsum):
        nonlocal answer
        if no >= len(numbers):
            if nsum == target:
                answer += 1
            return

        comb(no + 1, nsum + numbers[no])
        comb(no + 1, nsum - numbers[no])

    comb(0, 0)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
solution(numbers, target)