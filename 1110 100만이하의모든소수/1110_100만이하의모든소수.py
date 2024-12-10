# 1 이상 100만 이하의 모든 소수를 구하는 프로그램을 작성하라
# 이 문제는 입력이 없음 !!! 계속해서 소수를 출력하면 됨
# 에라토스테네스의 체 // 검색 후 답안 확인

n = 10 ** 6 + 1
data = [1] * n
data[0], data[1] = 0, 0

# 배수 처리
for i in range(2, n) :
    if data[i] == 1 :
        for j in range(i * 2, n, i) :
            data[j] = 0

for i in range(n) :
    if data[i] == 1 :
        print(i, end=' ')
