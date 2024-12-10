import sys
sys.stdin = open('쉬운거스름돈.txt',  'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    rst = 0
    ans = []

    for i in range(len(money)): # 0 ~ 7
        if money[i] <= N:
            rst = N // money[i] # 주어진 돈을 화폐단위로 정수 나눗셈 해줌
            N %= money[i] # 주어진 돈을 계속해서 나머지 연산해줌
            ans.append(rst) # 나머지를 빈 배열에 추가해줌
        else : # 화폐단위로 나눠지지 않으면 그 자리에는 0을 추가해줌
            ans.append(0)

    print(f'#{tc}')
    print(*ans)

# if문 달 필요 없이 이렇게 쓰면 됨 => 어차피 나머지 0 이면 알아서 저장되니깐
# for i in range(len(money)):
#      cnt = N // money[i]
#      N %= money[i]
#      arr.append(cnt)
#  print(f'#{tc}')
#  print(*arr)