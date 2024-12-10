import sys
sys.stdin = open('아름이의돌던지기.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = []
    # mm 단위로 -100,000 ~ 100,000 숫자가 일렬로 써져있음
    # 사람들은 숫자 100,000 위치에 서서 최대한 0에 가까운 위치로 돌을 던짐
    # N명의 사람들이 던진 돌이 떨어진 위치를 측정한 자료가 주어질 때
    # 가장 0에 가깝게 돌이 떨어진 위치 ~ 0 사이의 거리 차이
    # => 0이랑 가장 가까이 던진 놈 찾아서 0이랑 차이 구하자 (절대값?)
    # +) 몇명이 그렇게 돌을 던졌는지 찾아 !!
    # 일단 모두 0과의 차이를 찾자 . 그리고 min 값을 뽑자,
    # 그 min 값을 구해낸 인덱스 값의 놈으 수를 찾아서 뽑아내자
    check = 0 # 0과의 차이 찾자
    for i in range(len(arr)):
        check = abs(0 - arr[i])
        ans.append(check)
    min_v = min(ans)
    cnt = ans.count(min_v)
    print(f'#{tc} {min_v} {cnt}')
