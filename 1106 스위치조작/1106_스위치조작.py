import sys
sys.stdin = open('스위치조작.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    min_v = 987654321

    for i in range(N):
        if A[i] != B[i]:  # A B 다를 때를 확인하는 코드
            for j in range(i, N):
                A[j] = 1 - A[j]  # 0, 1 바꿔주는 코드 (A[i] + 1) % 2 해줘도 됨 !!
            cnt += 1
        else :
            continue

    if min_v > cnt:
        min_v = cnt

    print(f'#{tc} {min_v}')
    # 최소값 굳이 안 구하고 그리디로 풀이해도 된다함