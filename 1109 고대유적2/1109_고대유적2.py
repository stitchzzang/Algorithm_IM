import sys
sys.stdin = open('고대유적2.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    # 행
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:
                cnt = 0

    # 열
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if max_v < cnt:
                    max_v = cnt
            else:
                cnt = 0

    if max_v == 1:
        max_v = 0

    print(f'#{tc} {max_v}')
