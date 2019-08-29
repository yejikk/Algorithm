import sys
sys.stdin = open("workshop2.txt")

test = int(input())

for tc in range(1, test+1):
    strnumbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    case = input()
    strnums = list(map(str, input().split()))
    result = []

    for first in strnumbers:
        for second in strnums:
            if first == second:
                result.append(first)
    print(f'#{tc}')
    print(' '.join(result))