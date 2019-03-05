import sys
sys.stdin = open('반나누기.txt')

def scoresort(score, N):
    Nscore = score[:]
    Nsort = []
    for i in range(N):
        maxscore = i
        for j in range(i+1, N):
            if Nscore[j] > Nscore[maxscore]:
                maxscore = j
        Nscore[i], Nscore[maxscore] = Nscore[maxscore], Nscore[i]

    for i in range(1, len(Nscore)):
        if Nscore[i] not in Nsort:
            Nsort.append(Nscore[i])
    return Nsort

test = int(input())

for tc in range(1, test+1):
    N, Kmin, Kmax = map(int, input().split())
    score = list(map(int, input().split()))
    T = scoresort(score, N)
    flag = 1
    result = []
    for i in range(len(T)-1):
        T2 = T[i]
        for j in range(i+1, len(T)):
            classroom = [[] for _ in range(3)]
            flag = 0
            T1 = T[j]
            for num in score:
                if num >= T2:
                    classroom[0].append(num)
                elif num >= T1 and num < T2:
                    classroom[1].append(num)
                else:
                    classroom[2].append(num)
            lenmax = 0
            lenmin = 100000
            for i in range(3):
                if len(classroom[i]) > lenmax:
                    lenmax = len(classroom[i])
                if len(classroom[i]) < lenmin:
                    lenmin = len(classroom[i])

            if lenmin >= Kmin and lenmax <= Kmax:
                flag = 0
            else:
                flag = 1

            if flag == 0:
                result.append(lenmax-lenmin)

    if result == []:
        print(-1)
    else:
        result = min(result)
        print(result)