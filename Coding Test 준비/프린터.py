def solution(priorities, location):
    answer = 0
    seq = list(map(int, range(len(priorities))))

    while priorities:
        flag = 0
        work = priorities.pop(0)
        n = seq.pop(0)

        N = len(priorities)
        for i in range(N):
            if priorities[i] > work:
                flag = 1
                priorities.append(work)
                seq.append(n)
                break

        if not flag:
            answer += 1
            if n == location:
                break

    return answer

solution([1, 1, 9, 1, 1, 1], 0)
