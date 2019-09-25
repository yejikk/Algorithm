def comb(clothes, no, chk):
    global cnt
    N = len(clothes)

    if no >= N:
        print(chk)
        kind = []
        flag = 0
        for i in range(N):
            if chk[i] and clothes[i][1] not in kind:
                kind.append(clothes[i][1])
            elif chk[i] and clothes[i][1] in kind:
                flag = 1
                break
        if not flag:
            print(kind)
            cnt += 1
        return

    chk[no] = 1
    comb(clothes, no+1, chk)
    chk[no] = 0
    comb(clothes, no+1, chk)

    return cnt

def solution(clothes):
    answer = 0
    cnt = 0
    chk = [0] * len(clothes)
    answer = comb(clothes, 0, chk)
    print(answer)
    return answer

cnt = 0
clothes = 	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)
print(clothes)