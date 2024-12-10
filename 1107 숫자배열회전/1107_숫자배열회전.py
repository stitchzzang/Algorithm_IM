import sys
sys.stdin = open('숫자배열회전.txt', 'r')

def turn_array(arr):
    new_arr = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(arr[j][i]) # i j 하면 가로 -> 세로 / j i 하면 세로 -> 가로
        new_arr.append(row[::-1]) # 열의 순서를 바꿔서 각 열을 new_arr에 저장
    return new_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr1 = turn_array(arr)
    arr2 = turn_array(arr1)
    arr3 = turn_array(arr2)

    print(f'#{tc}')
    for i in range(N): # 90도 180도 270도 돌린 것들을 0행부터 차례로 다 뽑고 줄 띄우는 거임
        for a in range(N):
            print(arr1[i][a], end = '') # 한 행을 줄띄움 없이 한 줄에 출력
        print(' ', end='')
        for b in range(N):
            print(arr2[i][b], end='')
        print(' ', end='')
        for c in range(N):
            print(arr3[i][c], end='')
        print()

    # 90도 / 180도 / 270도 => 3번씩 해서 각 열에 저장함녀 되는데 어떻게 하지 ?
    # n열 -> n 행으로 바뀜 , 근데 시작 점을 반대로 해주자
    # 0열 => 0행 근데 반대로 열을 끝값부터 처음 값 까지 나오게
    # 열을 1차원 배열로 하나씩 저장, 저장하고 그걸 원래 배열의 행으로 만들자 ..
    # ok 여기까지 회전한 걸 만들었는데 // 각 행을 공백 없이 붙이고 0열에 저장해야됨
    # 이게 왤캐 어렵냐 ;;
    # 입력과 달리 출력에서는 회전한 모양 사이에서만 공백이 존재함에 유의
