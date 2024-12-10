import sys
sys.stdin = open('정곤이의단조증가하는수.txt', 'r')

# 입력의 곱들을 1자로 나열하기
# 그 중 단조인 수를 확인하고 최댓값 갱신하기

def check(v):
    s = str(v)
    for i in range(0, len(s) - 1):
        # 하나라도 단조 증가 하지 않으면 실패
        if s[i] > s[i + 1]:
            return False
    return True


# 테스트 케이스의 수
T = int(input())
for tc in range(1, T + 1):
    # 정수 개수
    N = int(input())
    # N개의 정수, A1,A2,....AN
    A = list(map(int, input().split()))
    # 내림차순으로 정리
    A.sort(reverse=True)

    # 가장 큰 값
    max_value = -1

    # Ai * Aj 구하기 ( 인데스는 0부터!!)
    for i in range(N - 1):
        for j in range(i + 1, N):
            value = A[i] * A[j]
            # 최댓값보다 작다면 할 필요 없음
            if max_value > value:
                break
            # 단조 증가 하는가?
            if check(value):
                max_value = value
    print(f'#{tc} {max_value}')