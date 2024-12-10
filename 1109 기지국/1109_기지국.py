import sys
sys.stdin = open('기지국.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    # 동서남북으로 탐색하니까 델타 탐색 써주자
    di = [0, -1, 0 ,1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if (0 <= ni < N) and (0 <= nj < N) and arr[ni][nj] == 'H':
                        arr[ni][nj] = 'X'
            elif arr[i][j] == 'B':
                for p in range(1, 3):
                    for k in range(4):
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        if (0 <= ni < N) and (0 <= nj < N) and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'
            elif arr[i][j] == 'C':
                for p in range(1, 4):
                    for k in range(4):
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        if (0 <= ni < N) and (0 <= nj < N) and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')

# 기지국에 커버되지 않는 집의 수를 출력
# 기지국의 위치와 집들이 표시된 지도 // 기지국에서 커버되지 않는 집의 수 찾기
# 각 기지국은 동서남북으로 1, 2, 3개의 셀을 커버 (동서남북)
# A : 1개 커버하는 기지국
# B : 2개 커버하는 기지국
# C : 3개 커버하는 기지국
# H : 집의 위치
# X : 아무 것도 없음

