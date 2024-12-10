import sys
sys.stdin = open('새로운불면증치료법.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서 0에서 9까지의 모든 숫자를 보게 되는가?
    # 그러면 N에 2부터 k까지 곱하고
    # 각 자릿수를 저장하자, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 인덱스 만들어서 저장하자
    # 인덱스에 저장된 숫자가 모두 1 이상이 되면 그때의 N * K 를 출력하자.
    N = int(input())
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 인덱스 번호로 저장
    k = 1

    while len(number) != 0: # number 배열이 비는 것 = 숫자를 모두 센 것
        m = N * k
        for j in str(m) :
            j = int(j) # 곱한 수가 문자열로 저장되어있으므로 숫자로 바꿔줌
            if j in number:
                number.remove(j) # 있는 숫자라면 number에서 제거해줌
        k += 1

    print(f'#{tc} {m}')

