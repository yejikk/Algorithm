def solution(progresses, speeds):
    answer = []
    time = 1
    cnt = 0

    while progresses:
        work = progresses[0] + (speeds[0] * time)
        if work >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            while progresses:
                task = progresses[0] + (speeds[0] * time)
                if task >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt += 1
                else:
                    break
            answer.append(cnt)
            cnt = 0

        time += 1

    return answer

solution([93, 30, 55], [1, 30, 5])