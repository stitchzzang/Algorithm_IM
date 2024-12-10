import sys
sys.stdin = open('기차사이의파리.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    print(f'#{tc} {(D / (A + B)) * F}')
    # 두 기차가 부딪힐 때 까지의 시간을 구함 (시간 = 거리/속력)
    # 그 시간에 파리의 속력을 곱해주면 이동거리 나옴
