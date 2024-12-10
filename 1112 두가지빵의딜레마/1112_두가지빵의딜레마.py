import sys
sys.stdin = open('두가지빵의딜레마.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    # if A > B :
    #     bread = B
    # else :
    #     bread = A

    bread = min(A, B)
    ans = C // bread

    print(f'#{tc} {ans}')

# 현미빵 A원, 단호박 빵 B원
# 은비는 C원 가지고 있음
# 어떤 빵이든 상관없음. 많은 개수의 빵을 사고싶음
# 두 종류의 개수를 다르게 사도 되고 한 종류만 사도 됨
# 최대 몇개의 빵을 살 수 있음 ?
