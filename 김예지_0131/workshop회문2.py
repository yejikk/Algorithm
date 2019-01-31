import sys
sys.stdin = open("workshop회문2.txt")

test = 10

for tc in range(1, test+1):
    case = int(input())
    arr = [[0]*100 for _ in range(100)]
    arrmax = 0

    for i in range(100):
        arr[i] = list(input())

    for i in range(100):
        rowarr = arr[i]
        for l in range(100):
            for j in range(1, 101): # 뒤집을 때 range 생각해야함
                if rowarr[l:j] == rowarr[l:j][::-1] and len(rowarr[l:j]) > arrmax:
                    arrmax = len(rowarr[l:j])

    for i in range(100):
        colarr = []
        for j in range(100):
            colarr.append(arr[j][i])
        for l in range(100):
            for k in range(1, 101):
                if colarr[l:k] == colarr[l:k][::-1] and len(colarr[l:k]) >= arrmax:
                    arrmax = len(colarr[l:k])

    print(f'#{tc} {arrmax}')
