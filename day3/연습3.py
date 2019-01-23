"""
9 20 20 18 11
19 1 25 3 21
8 24 10 17 7
15 4 16 5 6
12 13 22 23 14

"""
#def wall(x, y):

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

data = [[9, 20, 20, 18, 11], [19, 1, 25, 3, 21],
        [8, 24, 10, 17, 7], [15, 4, 16, 5, 6],
        [12, 13, 22, 23, 14]]

newlist = [[0 for _ in range(len(data))] for _ in range(len(data))]
leng = len(newlist) * len(newlist)
dx =

for i in range(leng):
    select = select_min(data)

    selmin = select[0]
    minX = select[1]
    minY = select[2]
    data[minX][minY] = 99

    if
