import sys
sys.stdin = open('농작물수확하기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 농장의 크기는 항상 홀수
    # 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능
    # 농장의 크기 N과 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 ?

    sum_v = 0
    start, end = N//2, N//2 # 여기까진 생각 했음
    for i in range(N):
        for j in range(start, end + 1):
            # 마름모 형태를 만들어 내려면 어떻게 해야할까
            # 중심을 기준으로 (0, N//2)에서 시작해서 중심을 만나기 전까지 양 옆 한칸 씩 늘려주고
            # 중심을 만난 뒤에는 양 옆 한칸씩 줄여주면 됨
            sum_v += arr[i][j]

        if i < N//2 :
            start -= 1
            end += 1

        else :
            start += 1
            end -= 1

    print(f'#{tc} {sum_v}')