import sys
sys.stdin = open("workshop01.txt")

T = 10

# def max_min(dump):
#     for i in range(len(dump)-1, 0, -1):
#         for j in range(0, i):
#             if dump[j] > dump[j+1]:
#                 dump[j], dump[j+1] = dump[j+1],

for tc in range(T):
    cnt = int(input())
    dump = list(map(int, input().split()))
    height_max = 0
    height_min = 101

