import sys
sys.stdin = open('파스칼의삼각형.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []

    for i in range(N):
        row = [1] * (i + 1)
        for j in range(1, i): # 인덱스 범위 찾는 것이 어려웠음 !!
            # 파스칼 삼각형의 첫째줄과 둘째줄은 1 / 1 1 고정임
            # 가로는 두번째 인덱스부터, 세로는 첫번째 인덱스부터 확인하면 되므로 1 ~ i-1 로 돌림
            row[j] = arr[i-1][j-1] + arr[i-1][j]
        arr.append(row)

    print(f'#{tc}')
    for row in arr: # 2차원 배열에서 한줄씩 뽑기
        print(*row) # packing 해서 출력