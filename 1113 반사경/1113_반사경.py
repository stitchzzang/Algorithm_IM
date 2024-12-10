import sys
sys.stdin = open('반사경.txt', 'r')

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    k = 0
    i = j = 0
    mirror = 0
    while True:
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 1:
                mirror += 1
                # 0->3, 1->2
                if k == 0:
                    k = 3
                elif k == 3:
                    k = 0
                elif k == 1:
                    k = 2
                elif k == 2:
                    k = 1
            elif arr[ni][nj] == 2:
                mirror += 1
                # 0->3, 1->2
                if k == 0:
                    k = 1
                elif k == 1:
                    k = 0
                elif k == 2:
                    k = 3
                elif k == 3:
                    k = 2
            i = ni
            j = nj
        else:
            break
    print(f'#{tc} {mirror}')