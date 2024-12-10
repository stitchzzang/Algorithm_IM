import sys
sys.stdin = open('스도쿠검증.txt', 'r')

def sudoku(arr):
    for i in range(9):
        sudoku_row = [0] * 10
        sudoku_col = [0] * 10
        for j in range(9):
            sudoku_row[arr[i][j]] += 1 # 가로 탐색
            if sudoku_row[arr[i][j]] == 2:
                return 0
            sudoku_col[arr[j][i]] += 1 # 세로 탐색 // j i 로 바꿔주기 주의
            if sudoku_col[arr[j][i]] == 2:
                return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sudoku_box = [0] * 10
            for k in range(3):
                for l in range(3):
                    sudoku_box[arr[k][l]] += 1 # 작은 격자 탐색
                    if sudoku_box[arr[k][l]] == 2:
                        return 0

    return 1


    # 스도쿠에 있는 숫자를 넣었을 때 1~9 로 개수를 세자.
    # 근데 개수가 2개 넘어가면 break 하고 return 0 하자


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {sudoku(arr)}')

