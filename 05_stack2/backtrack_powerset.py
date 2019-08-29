# 완전 검색으로 부분집합구하기
def process_solution(a, k): # 출력하는 함수
    result = []
    for i in range(1, k+1):
        if a[i]:
            result.append(data[i])
    print(result)

def make_candidates(a, k, input, c): # 0 또는 1일 경우를 계산해주기 위해서
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input): # backtraking아님 완전검색
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)

MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3]
a = [0] * NMAX
backtrack(a, 0, 3)