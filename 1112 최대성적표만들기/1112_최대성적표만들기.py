import sys
sys.stdin = open('최대성적표만들기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = list(map(int, input().split()))

    max_score = sorted(score, reverse=True)
    sum_v = 0
    for i in range(K):
        sum_v += max_score[i]

    print(f'#{tc} {sum_v}')