"""
3 4
0 1 0 0
0 0 0 0
0 0 1 0
"""

# 예시1
n, m = map(int, input().split())
mylist = [[0 for _ in range(m)] for _ in range(n)]# 밑줄은 무명 변수! 변수가 필요 없을 때

for i in range(n) :
    mylist[i] = list(map(int, input().split()))
print(mylist)