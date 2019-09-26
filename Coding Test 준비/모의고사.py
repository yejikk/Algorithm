def solution(answers):
    answer = []
    student = []

    student.append([1, 2, 3, 4, 5] * (10000 // 5))
    student.append([2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8))
    student.append([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000 // 10))
    cnt = [0] * 4

    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == student[i][j]:
                cnt[i+1] += 1

    nmax = 0
    idx = 0
    for i in range(1, 4):
        if cnt[i] > nmax:
            answer = []
            idx = i
            nmax = cnt[i]
            answer.append(i)
        elif nmax == cnt[i]:
            answer.append(i)

    return answer

solution([1,2,3,4,5])