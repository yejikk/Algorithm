import sys
sys.stdin = open("workshop.txt")

test = int(input())

match = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
         'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

def minvalue(result):
    for i in range(len(result)):
        Min = i
        for j in range(i+1, len(result)):
            if result[j] < result[Min]:
                Min = j
        result[i], result[Min] = result[Min], result[i]
    return result


for tc in range(1, test+1):
    case = input()
    strnumber = list(map(str, input().split()))
    result = []
    last = []
    # print(strnumber)

    for num in strnumber:
        for key, value in match.items():
            if num == key:
                result.append(value)
    result = minvalue(result)
    # print(result)

    for num in result:
        for key, value in match.items():
            if num == value:
                last.append(key)
    print(f'#{tc}')
    print(' '.join(last))
