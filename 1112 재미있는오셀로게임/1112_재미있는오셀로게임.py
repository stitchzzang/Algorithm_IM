import sys
sys.stdin = open('재미있는오셀로게임.txt', 'r')

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

# 보드판을 초기화
# 처음에 검은돌과 흰돌을 2개씩 놓는다.
def init(N):
    global board
    t_pos = N // 2
    board[t_pos - 1][t_pos - 1] = 2
    board[t_pos][t_pos] = 2
    board[t_pos][t_pos - 1] = 1
    board[t_pos - 1][t_pos] = 1


# 위치를 체크
def isWall(x, y, color):
    global N, board
    # 이동이 벽을넘어가면
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
        # 돌이 없으면
    if not board[x][y]:
        return 0
    # 자기 돌이라면
    if board[x][y] == color:
        return 2
    # 상대 돌이라면
    return 1


# 돌을 놓으면 데이터를 처리
def boardCheck(x, y, color):
    global board, dx, dy
    for i in range(8):
        # 어디방향으로 이동할지 설정한다.
        d_x = dx[i]
        d_y = dy[i]
        # 상대방 돌을 내돌로 바꾸는 리스트 생성
        change_list = []
        # 반복문을 통해 체크한다.
        while True:
            # 이동할 경로를 체크한다.
            a = isWall(x + d_x, y + d_y, color)
            # 리턴이 0일때이며, 돌이없거나 벽이동을 못할때이다.
            # 반복문을 종료한다.
            if not a: break
            # 나와 같은색상의 돌을 만났을때이다.
            if a == 2:
                # 지금까지 저장했던 상대방돌을 내돌로 바꾼다.
                # 반복문을 중지한다.
                for c_x, c_y in change_list:
                    board[c_x][c_y] = color
                break
            # 상대방의 돌을 만났을 때이다.
            # 리스트에 상대방 돌정보를 저장한다.
            if a == 1:
                change_list.append([x + d_x, y + d_y])
            # 반복이 진행될때마다 한칸씩 진행한다.
            d_x += dx[i]
            d_y += dy[i]
    # 놓은 돌을 처리한다.
    board[x][y] = color


# 돌 개수를 검사하는 함수
def w_b_count(N):
    global board, w_count, b_count
    # 2차원리스트를 돌면서 숫자를 체크한다.
    for i in board:
        b_count += i.count(1)
        w_count += i.count(2)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 보드판을 N X N만큼 0으로 초기화한다.
    board = [[0 for _ in range(N)] for _ in range(N)]
    # 초기화 함수를 불러 셋팅한다.
    init(N)
    # M번만큼 반복하여 입력받는다.
    for _ in range(M):
        x, y, color = map(int, input().split())
        # 돌을 받을때마다 데이터를 처리한다.
        boardCheck(x - 1, y - 1, color)
    # 돌의 개수를 체크한다.
    w_count = 0
    b_count = 0
    w_b_count(N)
    # 결과를 출력한다.
    print(f'#{tc} {b_count} {w_count}')