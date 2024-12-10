import sys
sys.stdin = open('특별한정렬.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # N 개의 정수가 주어지면
    # 가장 큰 수, 가장 작은 수, 두번째 큰 수, 두번째 작은 수 식으로
    # [1, 2, 3, 4] 있으면 1 4 2 3  이런 식으로 뽑아야됨
    # 내림차순 배열 하나, 오름차순 배열 하나 이렇게 정리해두고 i 돌 때 마다 출력하게끔 하자

    arr_max = sorted(arr, reverse=True)
    arr_min = sorted(arr)

    print(f'#{tc}', end= ' ')
    for i in range(5):
        print(f'{arr_max[i]}', end=' ')
        print(f'{arr_min[i]}', end=' ')
    print()