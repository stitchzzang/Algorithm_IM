import sys
sys.stdin = open('어디에단어가들어갈수있을까.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 흰색은 1, 검은색은 0으로 표시됨
    # 목표는 연속된 1의 길이가 K인 구간을 찾는 것

    ans = 0  # 정답 개수를 저장할 변수

    # 가로 방향으로 단어가 들어갈 수 있는 구간을 찾기
    for i in range(N):
        cnt = 0  # "연속된" 흰색 칸(1)의 개수를 세기 위한 변수
        for j in range(N):
            if arr[i][j] == 1:  # 흰색 칸일 경우
                cnt += 1  # 연속된 흰색 칸 수 증가
            else:  # 검은색 칸을 만나면
                # 이전에 세어둔 연속된 흰색 칸 수가 K와 같다면 단어를 넣을 수 있음
                if cnt == K: # 흰색 칸이 연속으로 이어진 구간이 만들어졌음
                    ans += 1 # ans = 단어를 넣음
                cnt = 0  # 칸 수 초기화

        # 행의 끝까지 갔을 때도 K와 같은 연속된 흰색 칸이 있는지 확인
        if cnt == K:
            ans += 1

    # 세로 방향으로 단어가 들어갈 수 있는 구간을 찾기
    for i in range(N):
        cnt = 0  # 연속된 흰색 칸(1)의 개수를 세기 위한 변수
        for j in range(N):
            if arr[j][i] == 1:  # 흰색 칸일 경우
                cnt += 1  # 연속된 흰색 칸 수 증가
            else:  # 검은색 칸을 만나면
                # 이전에 세어둔 연속된 흰색 칸 수가 K와 같다면 단어를 넣을 수 있음
                if cnt == K:
                    ans += 1
                cnt = 0  # 칸 수 초기화

        if cnt == K: # 한 줄이 다 끝났을 때 0을 안 만나더라도 K를 충족시킬 수 있기에 확인해야함
            ans += 1

    # 테스트 케이스 결과 출력
    print(f'#{tc} {ans}')