import sys
sys.stdin = open('간단한소인수분해.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [2, 3, 5, 7, 11]
    # [a, b, c, d, e]
    ans = [0, 0, 0, 0, 0]
    # num의 숫자 중에 하나로 나누어 떨어진다 ?
    # 일단 나누고 그다음에 또 나누어 떨어지는 걸 찾자
    for i in range(len(num)):
        while N % num[i] == 0: # 나누어 떨어질 때까지 반복
            ans[i] += 1
            N //= num[i]

    print(f'#{tc}', *ans)