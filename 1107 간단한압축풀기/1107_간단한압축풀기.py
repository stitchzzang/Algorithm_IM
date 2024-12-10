import sys
sys.stdin = open('간단한압축풀기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    ans = '' # 리스트 말고 str 로 받자 !!

    # 처음에 다 str로 받아야 함
    for i in range(N):
        num = int(arr[i][1]) # 숫자로 바꿔주고
        ans += arr[i][0] * num # 문자를 그 숫자만큼 곱해준다 / 문자열에 누적합 하자
    print(f'#{tc}')
    for j in range(0, len(ans), 10):
        print(ans[j:j+10])