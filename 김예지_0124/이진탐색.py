import sys
sys.stdin = open("이진탐색.txt")

test = int(input())

# A, B를 나눠서 변수를 선언하지 않고 함수하나 만들어놓고 2번 호출하면
# 코드가 더 간단해진다.
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