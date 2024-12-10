import sys
sys.stdin = open('파리퇴치3.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, -1, 0, 1] # 델타 탐색 - 가로
    dj = [1, 0, -1, 0] # 델타 탐색 - 세로
    dx = [1, -1, -1, 1] # 델타 탐색 대각선 - 가로
    dy = [1, 1, -1, -1] # 델타 탐색 대각선 - 세로

    max_v = 0

    # 가로 세로 탐색
    for i in range(N): # N X N 배열 탐색
        for j in range(N):
            sum_v = arr[i][j] # 합계 값 초기화
            for p in range(1, M):
                for k in range(4): # 델타 배열의 인덱스 0 부터 3까지
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if (0 <= ni < N) and (0 <= nj < N):
                        sum_v += arr[ni][nj]
            # sum_v 초기화 한 위치에서 최대값 구하면 된다!
            if max_v < sum_v:
                max_v = sum_v

            # 대각선 가로 세로 탐색
            sum_v2 = arr[i][j]
            for p2 in range(1, M): # M은 세기
                for k2 in range(4): # 델타 배열의 인덱스 0 부터 3까지
                    nx = i + dx[k2] * p2 # 세기의 값을 곱해줌
                    ny = j + dy[k2] * p2
                    if (0 <= nx < N) and (0 <= ny < N):
                        sum_v2 += arr[nx][ny]

            if max_v < sum_v2:
                max_v = sum_v2

    print(f'#{tc} {max_v}')