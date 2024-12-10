import sys
sys.stdin = open('가장빠른문자열타이핑.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())

    b = (len(B) - 1) * A.count(B) # 문자열 A에 B가 몇번 나오는지 셈
    ans = len(A) - b # A 길이에서 제거해야 하는 갯수 b (B 길이에서 눌러야하는 횟수 1 뺀 값에 나타난 횟수를 곱하면 됨)

    print(f'#{tc} {ans}')



