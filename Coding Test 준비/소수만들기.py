def solution(nums):
    answer = 0
    temp = [0] * len(nums)

    def prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def comb(no, cnt):
        nonlocal nums, temp, answer
        if cnt == 3:
            nsum = sum(temp)
            if prime(nsum):
                answer += 1
            return

        if no == len(nums):
            if cnt == 3:
                nsum = sum(temp)
                if prime(nsum):
                    answer += 1
            return

        temp[no] = nums[no]
        comb(no + 1, cnt + 1)
        temp[no] = 0
        comb(no + 1, cnt)

    comb(0, 0)
    return answer

print(solution([1, 2, 7, 6, 4]))