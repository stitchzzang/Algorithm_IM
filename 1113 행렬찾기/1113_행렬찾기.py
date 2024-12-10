import sys
sys.stdin = open('행렬찾기.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:  # sp
                # 행
                w = 0
                for k in range(j, N):
                    if arr[i][k] != 0:
                        w += 1
                    else:
                        break

                # 열
                h = 0
                for l in range(i, N):
                    if arr[l][j] != 0:
                        h += 1
                    else:
                        break

                lst.append((h, w))

                # 방문체크
                for v in range(h):
                    for k in range(w):
                        arr[i + v][j + k] = 0

    # 크기순 정렬
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            area_i = lst[i][0] * lst[i][1]
            area_j = lst[j][0] * lst[j][1]
            if area_i > area_j:
                lst[i], lst[j] = lst[j], lst[i]
            elif area_i == area_j:
                if lst[i][0] > lst[j][0]:
                    lst[i], lst[j] = lst[j], lst[i]

    # 결과 출력
    print(f"#{tc} {len(lst)}", end=' ')
    for n in lst:
        print(n[0], n[1], end=' ')
    print()