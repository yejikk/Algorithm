# 자기자신말고 배수 check 먼저하기
# check 당하지 않는 숫자가 소수
# check를 해서 미리 정보 셋팅을 해놓기
# 함수를 만들기 (check 함수) : 2중 loop를 통해서 check해주기

import sys
sys.stdin = open('소수의개수.txt')

def check(arr, b):
    # 배수
    for i in range(2, b+1):
        # root 이상이면 계산할필요 없음(해도되는데 시간이 오래걸림)
        if i*i > b:
            break
        else:
            # 숫자들 (자기 자신을 포함하면 안되기 때문에 i*2, 증가치를 i로 만들어놓음
            for j in range(i*2, b+1, i):
                if arr[j] == 1:
                    continue
                else:
                    arr[j] = 1
    return arr

# 배수 check를 위한 배열 (소수가 아니면 1로 check)
arr = [0]*100001

a, b = map(int, input().split())
if a > b:
    a, b = b, a

result = check(arr, b)
cnt = 0

for i in range(a, b+1):
    if i == 1:
        continue
    if arr[i] == 0:
        cnt += 1

for i in range(a, b+1):
    if i == 1:
        continue
    if arr[i] == 0:
        mins = i
        break

for j in range(b, 1, -1):
    if arr[j] == 0:
        maxs = j
        break

print(cnt)
print(mins+maxs)