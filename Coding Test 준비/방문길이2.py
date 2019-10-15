def solution(dirs):
    x = 0
    y = 0
    step = []
    for dir in dirs:
        if dir == "U":
            if y < 5:
                y += 1
                if ((x, y-1),(x, y)) not in step:
                    step.append(((x, y-1),(x, y)))
        elif dir == "D":
            if y > -5:
                y -= 1
                if ((x, y), (x, y+1)) not in step:
                    step.append(((x, y),(x, y+1)))
        elif dir == "L":
            if x > -5:
                x -= 1
                if ((x, y),(x+1, y)) not in step:
                    step.append(((x, y),(x+1, y)))
        elif dir == "R":
            if x < 5:
                x += 1
                if ((x-1, y),(x, y)) not in step:
                    step.append(((x-1, y),(x, y)))

    return len(step)
