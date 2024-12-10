import sys
sys.stdin = open('연속한1의개수.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    max_v = 0
    cnt = 0
    for i in range(N):
        if arr[i] == 1:
            cnt += 1  # 연속된 1을 카운트

        else:
            if max_v < cnt:  # 0이면 최대값 갱신해야됨
                max_v = cnt  # 연속된 1의 최대값 갱신
            # 0을 만나면 카운트를 초기화 // 끊어서 저장할 생각 하지말고 0을 만나면 초기화할 수 있도록 하자
            cnt = 0

    if max_v < cnt:
        max_v = cnt  # 마지막 연속된 1을 체크하기 위해 최종적으로 갱신

    print(f'#{tc} {max_v}')