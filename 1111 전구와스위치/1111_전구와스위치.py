import sys
sys.stdin = open('전구와스위치.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bulb = list(map(int, input()))
    target = list(map(int, input()))

    def change(A, B):
        L = A[:]
        press = 0
        for i in range(1, N):
            # 이전 전구가 같은 상태면 pass
            if L[i - 1] == B[i - 1]:
                continue
            # 상태가 다를 경우
            press += 1
            for j in range(i - 1, i + 2):
                if j < N:
                    L[j] = 1 - L[j]

        if L == B :
            return press
        else :
            return 1e9
        # return press if L == B else 1e9

    # 첫번째 전구의 스위치를 누르지 않는 경우
    res = change(bulb, target)
    # 첫번째 전구의 스위치를 누르는 경우
    bulb[0] = 1 - bulb[0]
    bulb[1] = 1 - bulb[1]
    res = min(res, change(bulb, target) + 1)

    if res != 1e9:
        res
    else :
        res = -1
    print(f'#{tc}', res)


# 뒤집는 게 나오는건 동일함
# 힌트
# N 개의 스위치와 N 개의 전구
# i번 스위치를 누르면 앞의 전구와 자기 전구와 뒤의 전구가 상태 변화함
# 1번은 1,2 번 바뀌고
# -1 번은 -1, -2번이 바뀜

# 맨 앞과 맨 뒤에 유의 !!
# 바로 앞의 값에 따라 바꿔주면 된다, 이걸 확인하자
# 1) 맨 앞쪽을 누를 때
# 2) 맨 앞쪽을 누르지 않을 때로 구분
# 앞에서부터 맞춰나가야 하는 그리디 문제임 !

