import sys
sys.stdin = open('workshop.txt')

def perm(n, k):
    global node, route, result, nmin, cx, cy, hx, hy
    if n == k:
        nsum = 0
        for j in range(1, len(node)):
            if j == 1:
                nsum += abs(cx - node[j-1][0]) + abs(cy - node[j-1][1])
            elif j == len(node)-1:
                nsum += abs(hx - node[j][0]) + abs(hy - node[j][1])
            nsum += abs(node[j-1][0] - node[j][0]) + abs(node[j-1][1] - node[j][1])
            if nsum > nmin:
                break
        if nsum < nmin:
            nmin = nsum

    else:
        for i in range(k, n):
            node[i], node[k] = node[k], node[i]
            perm(n, k+1)
            node[i], node[k] = node[k], node[i]

test = int(input())

for tc in range(1, test+1):
    N = int(input())
    route = list(map(int, input().split()))
    # print(route)
    cx, cy = route[0], route[1]
    hx, hy = route[2], route[3]
    route = route[4:]
    node = []
    for i in range(0, N*2, 2):
        node.append([route[i], route[i+1]])
    nmin = 99999999
    perm(len(node), 0)
    print('#{} {}'.format(tc, nmin))
