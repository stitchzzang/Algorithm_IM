import sys
sys.stdin = open('다솔이의다이아몬드장식.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    word = input()
    first_line = '..#.'
    second_line = '.#.#'
    third_line = '#.'
    third_line_2 = '.'

    print(first_line * len(word) + '.')
    print(second_line * len(word) + '.')
    for i in range(len(word)):
        print(third_line + word[i] +  third_line_2, end="")
        if i == len(word) - 1:
            print('#')
    print(second_line * len(word) + '.')
    print(first_line * len(word) + '.')

'''
결국엔 각 줄을 4개 단위로 끊어서 반복시키고
마지막에만 1글자를 추가시켜주는 방식으로 접근했다.
1. 첫번째 줄 '..#.'을 단어의 길이만큼 반복하고 마지막에 '.'을 추가
2. 두번째 줄, 네번째 줄, 다섯번째 줄도 마찬가지
3. 세번째 줄은 '#.' + 단어의 한 글자 + '.' 이렇게 단어의 길이만큼 반복 후 마지막에 '#' 추가
'''