import sys
sys.stdin = open('미로탈출로봇.txt')

def wall(tx, ty):
    global N, M, arr
    if tx < 0 or tx >= M: # 열
        return False
    if ty < 0 or ty >= N: # 행
        return False
    if arr[ty][tx] == 1:
        return False
    return True

def BFS(x, y):
    global arr, endx, endy
    dx = [0, 0, -1, 1] # 열이동
    dy = [-1, 1, 0, 0] # 행이동
    queue = []
    queue.append([x, y, 0]) # 열, 행, cnt
    # 1) 시작점 큐에 저장(방문표시)
    while queue: # 큐가 빌 때까지 반복
        # 2) 큐에서 데이터 읽기(현재 위치, 현재 시간)
        v = queue.pop(0)
        x = v[0]
        y = v[1]
        cnt = v[2]
        # 3) 사방 탐색하면서 연결점(길)을 찾아 큐에 저장
        for i in range(4):
            tx = x + dx[i] # 열
            ty = y + dy[i] # 행
            if wall(tx, ty):
                if tx == endx and ty == endy:
                    return cnt + 1
                else:
                    queue.append([tx, ty, cnt+1])
                    arr[ty][tx] = 1
            # 3-1) 맵 범위 이내 여부 체크
            # 3-2) 연결점을 찾아서 큐에 저장 (방문 표시)
    # 4) 큐가 비었을 경우
    return -1

M, N = map(int, input().split())
startx, starty, endx, endy = map(int, input().split())
startx = startx - 1
starty = starty - 1
endx = endx - 1
endy = endy - 1

arr = [[0]*M for _ in range(N)]
for k in range(N):
    arr[k] = list(map(int, input()))

sol = 9999999
while True:
    result = BFS(startx, starty) # 열, 행
    if result == -1:
        break

    if result < sol:
        sol = result

print(sol)