import sys
sys.stdin = open('풍선팡.txt', 'r')

# N줄에 걸쳐 M개씩 든 풍선에 든 종이 꽃가루 수가 주어짐
# 종이 꽃가루의 최대 개수를 곱해야 됨 // 네방향으로 풍선이 터짐 = 총 5개 풍선 터짐

T = int(input())
for tc in range(1, T+1):
    di = [0, -1, 0, 1] # 델타 탐색 - 가로
    dj = [1, 0, -1, 0] # 델타 탐색 - 세로
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    for i in range(n):
        for j in range(m):
            sum_v = arr[i][j]
            for p in range(1, arr[i][j]+1):
                for k in range(4):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if (0 <= ni < n) and (0 <= nj < m):
                        sum_v += arr[ni][nj] # 중앙값에 네방향 탐색 값을 누적합 해줌

            if max_v < sum_v: # 최대값 찾기
                max_v = sum_v

    print(f'#{tc} {max_v}')