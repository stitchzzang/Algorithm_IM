import sys
sys.stdin = open('민석이의과제체크하기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # 몇 명의 학생이 있는지, 몇 명이 제출했는지
    std = list(map(int,input().split())) # 제출한 사람 리스트
    arr = []
    for i in range(1, N+1):
        arr.append(i) # 빈 리스트 arr에 학생 수 만큼 번호대로 리스트 만듦
        for j in range(len(arr)): # arr의 학생 중에 std에 속한 애가 있다면 빼줘야 함
            if arr[j] in std:
                arr.remove(arr[j])

    print(f'#{tc}', *arr)
    # *arr 리스트 한 꺼번에 출력
    # packing은 여러개의 객체를 하나의 객체로 합쳐줌