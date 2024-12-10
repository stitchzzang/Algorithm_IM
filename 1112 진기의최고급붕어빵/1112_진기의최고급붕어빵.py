import sys
sys.stdin = open('진기의최고급붕어빵.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # 손님 수 N, M 초에, K 개씩
    arr = list(map(int, input().split())) # N명의 손님 도착 시간

    arr.sort()
    result = "Possible"

    for i in range(N):
        boong = (arr[i] // M) * K # arr[i] 시간까지 만들 수 있는 붕어빵
        if boong < i+1 : # i+1 번째 손님
            result = "Impossible"
            break
    print(f'#{tc} {result}')

    # 0초 이후 손님들이 언제 도착하는지 주어지면
    # 모든 손님들에게 기다리는 시간 없이 붕어빵을 있는 지 판별
    # 대기 시간 없이 제공 가능 Possible, 아니면 Impossible

    # 2 2 2 / 1 2 의 경우
    # 2명의 사람에게 제공, 2초에 2개씩 만들어 냄
    # 1초에 도착, 2초에 도착 => 바로 제공 불가능 ! = Impossible



