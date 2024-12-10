import sys
sys.stdin = open('영준이의카드카운팅.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    now = input() # 현재 영준이가 가지고 있는 카드의 정보
    ans = []

    for i in range(0, len(now), 3):
        j = i + 3
        ans.append(now[i:j]) # 세개 씩 끊어서 저장

    card = [13, 13, 13, 13]
    if len(set(ans)) != len(ans):
    # 중복 처리한 배열이 원래의 배열과 길이가 다름 => 중복 존재
        card = 'ERROR'

    else:
        for i in ans: # ans에서 하나씩 끊어서 비교
            if i[0] == 'S':
                card[0] -= 1
            elif i[0] == 'D':
                card[1] -= 1
            elif i[0] == 'H':
                card[2] -= 1
            else:              # i[0] == 'C':
                card[3] -= 1

    if card == 'ERROR':
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc}', *card)
