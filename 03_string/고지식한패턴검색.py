# 연습문제 3

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    M = len(p) # 찾을 패턴의 길이
    N = len(t) # 전체 텍스트의 길이

    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M # 검색 성공
    else: return -1 # 검색 실패

def BruteForce2(text, pattern):
    for i in range(len(text)-len(pattern))
        

p = "TTA" # 찾을 텍스트
t = "TTTTTA" # 전체 텍스트
print(BruteForce(p, t))

# find 메소드 사용하면 바로 나옴
print(t.find(p))