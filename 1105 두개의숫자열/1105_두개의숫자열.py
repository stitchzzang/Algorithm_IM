import sys
sys.stdin = open('두개의숫자열.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_v = 0

    for i in range(abs(M-N)+1): # A배열의 크기 만큼 구간을 돌아야 하므로 N-M+1
        sum_v = 0
        if N < M :
            j = i + N
            new_arr = B[i:j] # 0 1 2 돌아가잖아 3 6 -7 얘를 1 5 3 각각 곱해서 저장해야됨
            for k in range(N):
                sum_v += (A[k] * new_arr[k])

            if max_v < sum_v:
                max_v = sum_v
        else : # 배열 길이에 따라서 값이 달라지니까 i, j 말고 A, B를 바꿔줘야됨
            j = i + M
            new_arr = A[i:j]
            for k in range(M):
                sum_v += (B[k] * new_arr[k])

            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')
