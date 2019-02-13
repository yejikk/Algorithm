import sys
sys.stdin = open("회문_input.txt")

test = int(input())

def arreverse(arry):
    newarr = arry[:]
    for i in range(len(arry)//2):
        x = newarr[i]
        newarr[i] = newarr[len(newarr)-1-i]
        newarr[len(newarr)-1-i] = x
    if newarr == arry:
        return arry

for tc in range(1, test+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    # 문자열로 입력 받아보기!
    # 2차원 배열이 아니라 문자열로 입력 받아도 된다.
    # 문자열이 시퀀스 type이라 indexing이 가능하기 때문에 2차원 배열로 받은 것과 똑같다.
    result = []

    for i in range(N):
        arr[i] = list(input())
    
    # 문자열 뒤집기로 앞과 뒤를 비교하는 code로도 회문을 풀 수 있음.
    # 문자열 뒤집기로 문제 풀어보기!
    for i in range(N):
        rowarr = arr[i][:]
        for j in range(N-M+1):
            old = rowarr[j:M+j][:]
            newarr = arreverse(old)
            if newarr:
                result = old
                break

    # flag라는 변수를 선언하여 1이면 아예 열은 for문이 안 돌아가게 만들어 보기
    # flag라는 변수를 선언할 수 있다는 것을 기억하기
    if bool(result) == False:
        for j in range(N):
            colarr = []
            for i in range(N):
                colarr.append(arr[i][j])
            for k in range(N-M+1):
                old = colarr[k:M+k][:]
                newarr = arreverse(old)
                if newarr:
                    result = old
                    break

    result = ''.join(result)
    print(f'#{tc} {result}')