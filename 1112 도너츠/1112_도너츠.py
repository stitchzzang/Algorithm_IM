import sys
sys.stdin = open('도너츠.txt','r')

def get_sum(i, j, k):
    sum_v = 0
    for p in range(k):
        for l in range(k):
            sum_v += arr[i+p][j+l]
    return sum_v

T = int(input())
for tc in range(1, T+1):
    N, M, k = list(map(int, input().split()))
    arr = [list((map(int, input().split()))) for _ in range(N)]

    max_v = 0
    # 구간합이라고 무작정 N-M+1 하지마라
    # 구간의 크기만큼 빼줘야하니까 N-k+1 M-k+1 해야됨
    for i in range(N-k+1): # 구간합 응용, 가로 N에서 그물 크기 k 만큼 빼주기
        for j in range(M-k+1): # 구간합 응용, 세로 N에서 그물 크기 k 만큼 빼주기
            big = get_sum(i, j, k)
            small = get_sum(i+1, j+1, k-2)
            # 시작점 (0, 0) 기준으로 (1, 1) 이라고 생각하면 기준점에서 (1, 1)부터 배열 돌리니깐 ㅇㅇ
            ans = big - small
            if max_v < ans:
                max_v = ans
    print(f'#{tc} {max_v}')