time = 250

Atime = 300
Btime = 60
Ctime = 10

result = [0, 0, 0]
flag = 0

while time > 0:
    if time // 300:
        result[0] += time // 300
        time = time - (300 * (time//300))

    elif time // 60:
        result[1] += time // 60
        time = time - (60 * (time//60))

    elif time // 10:
        result[2] += time // 10
        time = time - (10 * (time//10))

    if time > 0 and time < 10:
        flag = 1
        break

    if time == 0:
        break

if flag:
    print(-1)
else:
    print(' '.join(map(str, result)))
