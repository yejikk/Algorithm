def printlist(data, bit):
    for i in range(len(bit)):
        if bit[i]:
            print(data[i], end=' ')
    print()

data = [1, 2, 3, 4]
# bit가 들어가 있는지 확인하기 위해서 data 리스트를 만들어줌
bit = [0, 0, 0, 0]

# 이 방법은 bit가 10개라면 for문을 10번 돌려야해서 무리가 있음
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
                printlist(data, bit)