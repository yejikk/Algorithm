import sys
sys.stdin = open("이진탐색.txt")

test = int(input())

def binarysearch(page, pa, pb):
    Aleft = 1
    Aright = page
    Bleft = 1
    Bright = page

    while (Aleft <= Aright) and (Bleft <= Bright):
        Amiddle = (Aleft + Aright) // 2
        Bmiddle = (Bleft + Bright) // 2

        if (pa == Amiddle) and (pb == Bmiddle):
            return 0
            break

        if pa == Amiddle and pb != Bmiddle:
            return 'A'
            break
        elif pa < Amiddle:
            Aright = Amiddle
        else:
            Aleft = Amiddle

        if pb == Bmiddle and pa != Amiddle:
            return 'B'
        elif pb < Bmiddle:
            Bright = Bmiddle
        else:
            Bleft = Bmiddle

    return 0
for tc in range(1, test+1):
    page, pa, pb = map(int, input().split())
    result = binarysearch(page, pa, pb)

    print(f'#{tc} {result}')