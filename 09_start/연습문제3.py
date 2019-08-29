asc = [[0,0,0,0],
        [0,0,0,1],
        [0,0,1,0],
        [0,0,1,1],
        [0,1,0,0],
        [0,1,0,1],
        [0,1,1,0],
        [0,1,1,1],
        [1,0,0,0],
        [1,0,0,1],
        [1,0,1,0],
        [1,0,1,1],
        [1,1,0,0],
        [1,1,0,1],
        [1,1,1,0],
        [1,1,1,1]]

pattern = [[0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1],
           [1, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1], [1, 1, 0, 1, 1, 1],
           [0, 0, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 1],
           [1, 0, 1, 1, 1, 1]]

def aToh(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])

t = []
arr = '0269FAC9A0'
for i in range(len(arr)):
    makeT(aToh(arr[i]))

result = []
idx = 0
while idx+6 < len(t):
    flag = 0
    for i in range(len(pattern)):
        if pattern[i] == t[idx:idx+6]:
            flag = 1
            result.append(i)
            idx = idx + 6
            break
    if flag == 0:
        idx += 1
print(''.join(map(str, result)))