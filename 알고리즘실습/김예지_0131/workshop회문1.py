import sys
sys.stdin = open("workshop회문1.txt")

test = 10

def palindrome(alpha):
    newalpha = alpha[:]
    for i in range(len(newalpha)//2):
        x = newalpha[i]
        newalpha[i] = newalpha[len(newalpha)-1-i]
        newalpha[len(newalpha)-1-i] = x
    return newalpha

for tc in range(1, test+1):
    length = int(input())
    arr = [[0]*8 for _ in range(8)]
    cnt = 0

    for i in range(8):
        arr[i] = list(input())

    for i in range(8):
        rowarr = arr[i]
        for j in range(8-length+1):
            new = palindrome(rowarr[j:length+j])
            if rowarr[j:length+j] == new:
                cnt += 1
    for i in range(8):
        colarr = []
        for j in range(8):
            colarr.append(arr[j][i])
        for k in range(8-length+1):
            new = palindrome(colarr[k:length+k])
            if colarr[k:length+k] == new:
                cnt += 1
    print(f'#{tc} {cnt}')