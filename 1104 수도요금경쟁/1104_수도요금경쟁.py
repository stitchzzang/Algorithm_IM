import sys
sys.stdin = open('수도요금경쟁.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    result = 0
    Amoney = 0
    Bmoney = 0

    Amoney = P * W # 종민이의 사용량 * P (1리터 당 요금)
    if W <= R : # R 과금 기준 리터 보다 사용량이 더 적으면
        Bmoney = Q # B사의 기본 요금만 냄
    elif W > R : # 과금 기준 리터보다 사용량이 더 많으면
        Bmoney = Q + ((W - R) * S) # 기본요금 + ((사용량 - 기준리터) * S (리터당 요금) )

    if Amoney > Bmoney:
        result = Bmoney
    else:
        result = Amoney
    print(f'#{tc} {result}')


    # P : A사의 1리터 당 요금
    # Q : B사의 기본 요금
    # R : 월간 사용량 과금 기준 리터
    # S : 월간 사용량 초과시 1리터 당 요금
    # W : 종민이의 월간 사용량 리터

    # A사의 요금 = (리터 양 * P)
    # B사의 요금 = Q (기본 요금) / Q + (리터 양 * S)


    # A사 = 1리터 당 P원의 돈
    # B사 = 기본 요금 Q원,
    # 월간 사용량이 R리터 이하 => 기본 요금
    # 월간 사용량이 R리터 초과 => 초과량에 대해 (1리터 당 S)원 더 내야 함
