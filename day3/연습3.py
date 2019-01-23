def wall(newlist, x, y):
    if (x < 0 or x >= 5) or (y < 0 or y >= 5): return False
    # if y < 0 or y >= 5: return False
    else :
        if newlist[x][y] != 0: return False
        else : return True

    return True

def select_min(data):
    min = 100
    minX = 0
    minY = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] < min:
                min = data[i][j]
                minX = i
                minY = j

    return min, minX, minY

data = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21],
        [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]

newlist = [[0 for _ in range(len(data))] for _ in range(len(data))]
leng = len(newlist) * len(newlist)

direction = 0
x = 0
y = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for i in range(leng):
    select = select_min(data)

    selmin = select[0]
    minX = select[1]
    minY = select[2]
    data[minX][minY] = 99

    if direction % 4 == 0:
        newlist[x][y] = selmin
        x += dx[0]
        y += dy[0]
        if wall(newlist, x, y) == False:
            direction += 1
            y -= 1
            x += 1

    elif direction % 4 == 1:
        newlist[x][y] = selmin
        x += dx[1]
        y += dy[1]
        if wall(newlist, x, y) == False:
            direction += 1
            x -= 1
            y -= 1

    elif direction % 4 == 2:
        newlist[x][y] = selmin
        x += dx[2]
        y += dy[2]
        if wall(newlist, x, y) == False:
            direction += 1
            x -= 1
            y += 1

    elif direction % 4 == 3:
        newlist[x][y] = selmin
        x += dx[3]
        y += dy[3]
        if wall(newlist, x, y) == False:
            direction += 1
            x += 1
            y += 1
print(newlist)