import sys
sys.stdin = open('오름차순정렬.txt')

def Msort(s, e):
    global N, number, temp
    if s >= e:
        return

    m = (s+e) // 2
    Msort(s, m)
    Msort(m+1, e)
    i = s # left
    j = m+1 # right
    k = s # idx 저장

    while i <= m and j <= e:
        # 왼쪽, 오른쪽 영역을 나누어서 임시버퍼에 비교한 후 저장
        if number[i] < number[j]:
            temp[k] = number[i]
            k += 1
            i += 1
        else:
            temp[k] = number[j]
            k += 1
            j += 1

    while i <= m: # 왼쪽 영역에 숫자가 남아있으면 임시버퍼에 저장
        temp[k] = number[i]
        k += 1
        i += 1

    while j <= e: # 오른쪽 영역에 숫자가 남아있으면 임시버퍼에 저장
        temp[k] = number[j]
        k += 1
        j += 1

    # 끝나고 원본 배열에 copy
    for i in range(s, e+1):
        number[i] = temp[i]

N = int(input())
number = list(map(int, input().split()))
temp = [0]*N

Msort(0, N-1)

print(' '.join(map(str, number)))