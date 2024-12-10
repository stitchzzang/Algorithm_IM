import sys
sys.stdin = open('사냥꾼.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 0 빈 공간, 1 사냥꾼, 2 토끼, 3 바위
    # 사냥꾼 - 상하좌우 및 대각선 8방향으로 사격, 총알 개수 무제한
    # 사냥꾼끼리 서로 사격할 수 없음, 바위 뒤편의 토끼는 사냥할 수 없음
    # 주어진 배열에서 사냥꾼이 총 몇 마리의 토끼를 사냥할 수 있는 지 구해라

    di = [0, -1, -1, -1, 0, 1, 1, 1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                for k in range(8): # k랑 p 순서 다르게 적지 말 것 !! / 방향을 고정한 후 점진적으로 늘려야 함
                    for p in range(1, N): # 대각선 범위를 어떻게 지정할 지
                            ni = i + di[k] * p
                            nj = j + dj[k] * p
                            if (0 <= ni < N) and (0 <= nj < N):
                                if arr[ni][nj] == 1 or arr[ni][nj] == 3: # 사냥꾼이나 바위를 만나면 중지
                                    break
                                if arr[ni][nj] == 2: # 토끼를 만나면 4로 바꿔줌
                                    arr[ni][nj] = 4

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 4: # 사냥된 토끼 = 4, 4의 개수를 출력
                cnt += 1

    print(f'#{tc} {cnt}')