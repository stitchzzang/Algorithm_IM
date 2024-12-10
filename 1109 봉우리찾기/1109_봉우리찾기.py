# import sys
# sys.stdin = open('봉우리찾기.txt', 'r')
# magnetic
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0

    if len(arr) == 1:
        if arr[0] == 0:
            cnt = 0
        else :
            cnt = 1

    else :
        flag = False
        for i in range(N-1):
            # new_arr = arr[i-1:i+2] # 3개씩 끊으면 안 될 듯
            if arr[i] < arr[i+1] :
                flag = True
                continue

            if flag == True and arr[i] > arr[i+1]:
                cnt += 1
                flag = False

        if arr[0] > arr[1]:
            cnt += 1

        if arr[-1] > arr[-2] :
            cnt += 1

    print(f'#{tc} {cnt}')

# 강사님 풀이
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     flag = 1
#
#     for i in range(N-1):
#         if flag == 0 and arr[i] < arr[i+1]:
#             flag = 1
#         elif flag == 1 and arr[i] > arr[i+1]:
#             flag = 0
#             cnt += 1
#     if flag :
#         cnt += 1
#     print(f'#{tc} {cnt}')