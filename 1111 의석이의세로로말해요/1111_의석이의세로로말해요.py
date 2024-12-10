import sys
sys.stdin = open('의석이의세로로말해요.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(str, input())) for _ in range(5)]
    ans = []
    max_row = 0

    for i in range(5):
        max_row = max(max_row, len(arr[i]))

    for j in range(max_row): # 열의 수는 가장 긴 행에 맞춰서 반복
        for i in range(5):
            # 행의 길이 > 열의 숫자
            # 각 행(arr[i])의 길이가 j보다 크면 그 열에 문자가 있다는 뜻
            # j가 행의 길이보다 길면, 그 행에 해당 열이 없으므로 건너 뛰자
            if j < len(arr[i]):
                ans.append(arr[i][j])
                # 단, 만약 현재 열의 문자가 해당 행에 없다면 (즉, 그 행의 길이가 짧다면) 그 문자는 건너뜀

    print(f'#{tc}', ''.join(ans))

# 다시 그 아래 쪽에 글자들을 붙여서 또 다른 단어를 만듦 / 이런 식으로 다섯개의 단어를 만듦
# A B C D E
# a b c d e
# 0 1 2 3 4
# F G H I J
# f g h i j

# A A B C D D 이렇게 길이가 안 맞으면 어떻게 해야하지 ?
# a f z z
# 0 9 1 2 1
# a 8 E W g 6
# P 5 h 3 k x