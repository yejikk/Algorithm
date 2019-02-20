# 완전 검색으로 순열구하기
def process_solution(a, k): # 출력하는 함수
    for i in range(1, k+1):
        print(data[a[i]], end=' ')
    print()

def make_candidates(a, k, input, c): # 사용한 번호는 재사용할 수 없기 때문에 check
    in_perm = [False] * NMAX

    for i in range(1, k):
        in_perm[a[i]] = True

    ncands = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncands] = i
            ncands += 1
    return ncands

def backtrack(a, k, input): # backtraking아님 완전검색
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k) # 답이면 원하는 작업
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