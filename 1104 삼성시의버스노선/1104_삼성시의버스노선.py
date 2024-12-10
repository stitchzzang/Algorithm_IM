import sys
sys.stdin = open('삼성시의버스노선.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    station = [0] * 5001 # 1번부터 5001번까지 5000개의 노선을 확인하기 위함

    for i in range(N):
        a, b = map(int, input().split())
        for j in range(a, b+1):
            station[j] += 1

    P = int(input())
    ans = []
    for k in range(P):
        c = int(input())
        ans.append(station[c])

    print(f'#{tc}', *ans)

