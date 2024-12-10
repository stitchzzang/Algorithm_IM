import sys
sys.stdin = open('오목판정.txt', 'r') # 시험 칠 때는 import sys 절대 넣으면 안 된다

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    di = [0, -1, -1, -1]
    dj = [1, 1, 0, -1]

    cnt = 0
    omok = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(4):
                    cnt = 1 # 네 방향 탐색을 시작할 때 초기화해야함, 위치 중요
                    for p in range(1, 5): # 대각선으로 1개 ~ 4개 체크하면 됨 = 오목 완성
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        if (0 <= ni < N) and (0 <= nj < N) and arr[ni][nj] == 'o': # 무조건 인덱스 체크 먼저 할 것
                            cnt += 1
                        else :
                            break

                        if cnt >= 5 :
                            omok = 1
                            break

    if omok == 1:
        print(f'#{tc} YES')
    else :
        print(f'#{tc} NO')