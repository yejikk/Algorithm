import sys
sys.stdin = open('주사위던지기2.txt')

# 순열
def DFS1(no, nsum):
    if no>N:
        if nsum == M:
            for i in range(1, N+1) :
                print(arr[i], end=" ")
            print()
        return
    for i in range(1, 7):
        if chk[i] == 1 :
            continue
        chk[i] == 1 # 눈 사용 체크
        arr[no] = i # 눈 기록
        DFS1(no+1, nsum + arr[no])


# 중복 배제 순열
def DFS2(no):
    if no>N:
        for i in range(1, N+1) :
            print(arr[i], end=" ")
        print()
        return
    for i in range(1, 7):
        if chk[i] == 1 :
            continue
        chk[i] == 1 # 눈 사용 체크
        arr[no] = i # 눈 기록
        DFS2(no+1)
        chk[i] = 0 # 눈 체크 해제


# 주사위 던진 횟수, 눈의 합
N, M = map(int, input().split())
dice = [0, 1, 2, 3, 4, 5, 6]
arr = [0]*8 # 주사위별 눈 기록 배열
chk = [0]*7
#DFS(1) # 1번 주사위부터 시작
# DFS1(1, 0)
DFS2(1)



# def DFS(no):
#     if no > N:
#         for i in range(1, N+1):
#             print(arr[i], end=' ')
#         print()
#         return
#     for i in range(1, 7): ## 1~6까지의 눈
#         arr[no] = i  # 눈 기록
#         DFS(no + 1)
#
# def DFS2(no):
#     if no > N:
#         for i in range(1, N+1):
#             print(arr[i], end=' ')
#         print()
#         return
#
#     for i in range(1, 7): ## 1~6까지의 눈
#         if chk[i] == 1:
#             continue
#         chk[i] = 1  # 눈 사용 체크
#         arr[no] = i  # 눈 기록
#         DFS2(no + 1)
#         chk[i] = 0  # 눈 체크 해제
#
# N, M = map(int, input().split())
# arr = [0] * 8  # 주사위별 눈 기록
# chk = [0] * 7
# # DFS(1)
# DFS2(1)