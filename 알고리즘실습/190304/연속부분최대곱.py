import sys
sys.stdin = open('연속부분최대곱.txt')

N = int(input())
number = []
for i in range(N):
    number.append(float(input()))

maxnum = 0
# for i in range(N):
#     mul = 1
#     if number[i] >= 1:
#         for j in range(i, N):
#             mul *= number[j]
#             if mul > maxnum:
#                 maxnum = mul
mul = 1
for i in range(N):
    if mul*number[i] < number[i]:
        mul = number[i]
    else:
        mul *= number[i]
    if mul > maxnum:
        maxnum = mul

print('%.3f' %maxnum)