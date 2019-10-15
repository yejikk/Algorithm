def solution(dirs):
    answer = 0
    temp = [[0] * 11 for _ in range(11)]
    x, y = 5, 5

    def wall(tx, ty):
        if tx < 0 or tx >= 12 or ty < 0 or ty >= 12:
            return False
        return True

    step = []
    for dir in dirs:
        if dir == 'U':
            if wall(x, y-1):
                y -= 1
                if ['U', x, y] not in step:
                    step.append(['U', x, y])
                    answer += 1
        elif dir == 'D':
            if wall(x, y+1):
                y += 1
                if ['D', x, y] not in step:
                    step.append(['D', x, y])
                    answer += 1
        elif dir == 'L':
            if wall(x-1, y):
                x -= 1
                if ['L', x, y] not in step:
                    step.append(['L', x, y])
                    answer += 1
        elif dir == 'R':
            if wall(x+1, y):
                x += 1
                if ['R', x, y] not in step:
                    step.append(['R', x, y])
                    answer += 1
    return answer

print(solution('LRUD'))