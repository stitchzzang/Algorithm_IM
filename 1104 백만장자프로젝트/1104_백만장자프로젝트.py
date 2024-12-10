import sys
sys.stdin = open('백만장자프로젝트.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    check = arr[N - 1]  # 기준점을 마지막 값으로 고정해두자

    for i in range(len(arr)-2, -1 ,-1): # 주의 : range(n, -1, -1) 이면 끝 값이 0임
        # 끝 값이 기준점으로 고정되어있으니 끝에서 두번째 값부터 비교하자
        # 기준점 보다 비교값이 작으면 ( 기준점 - 비교값 ) 이 값을 일단 저장해두자
        if arr[i] < check :
            ans += (check - arr[i]) # 이걸 빼잖아 .. 근데 기준을 어케 잡음 ?
        # 만약 기존 기준점보다 더 큰 값을 만났다 = 기준점을 바꿔줘야함
        else :
            check = arr[i]

    print(f'#{tc} {ans}')

