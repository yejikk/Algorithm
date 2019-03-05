import sys
sys.stdin = open('도약.txt')

N = int(input())
leaf = []
for i in range(N):
    leaf.append(int(input()))

leaf.sort()
print(leaf)

for i in range(N):
    