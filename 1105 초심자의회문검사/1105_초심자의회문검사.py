import sys
sys.stdin = open('초심자의회문검사.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    palindrome = str(input())
    p_lst = list(palindrome)
    pp_lst = p_lst[::-1]
    if p_lst == pp_lst:
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')