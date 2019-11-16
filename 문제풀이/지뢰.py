def solution(board, y, x):
    answer = []
    for i in range(len(board)):
        board[i] = list(board[i])

    def wall(ty, tx):
        nonlocal board
        if ty < 0 or ty >= len(board) or tx < 0 or tx >= len(board[i]):
            if ty < 0 or ty >= len(board) or tx < 0 or tx >= len(board[i]):
                return False
            return True

    def dfs(y, x):
        nonlocal board
        dx = [-1, 1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, -1, 1, 1, -1, 1, -1]
        temp = [[y, x]]

        while temp:
            y, x = temp.pop()
            if board[y][x] == 'E':
                cnt = 0
                for i in range(8):
                    ty = y + dy[i]
                    tx = x + dx[i]
                    if wall(ty, tx):
                        if board[ty][tx] == 'M':
                            board[ty][tx] == 'E'
                            cnt += 1
                        elif board[ty][tx] == 'E':
                            temp.append([ty, tx])

                if cnt > 0:
                    board[y][x] = cnt
                else:
                    board[y][x] = 'B'

        answer = board
        return answer

    if board[y][x] == "M":
        board[y][x] == "X"
        result = board
    else:
        result = dfs(y, x)

    for i in range(len(result)):
        result[i] = ''.join(map(str, result[i]))

    return result


print(solution(["EEEEE", "EEMEE", "EEEEE", "EEEEE"], 2, 0))

