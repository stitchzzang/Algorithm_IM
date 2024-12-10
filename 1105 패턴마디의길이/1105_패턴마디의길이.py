import sys
sys.stdin = open('패턴마디의길이.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    stc = str(input()) # 문자열(문장) 입력 받음
    lst = list(stc) # 문자열을 리스트로 바꾸자
    new_lst = [lst[0]] # 첫번째는 무조건 같으니까 저장해줘야함

    for i in range(1, len(lst)):
        if new_lst[0] == lst[i]:
            # idx[0]을 만나기 전의 길이(저장해둔 거)만큼 비교해주면 된다
            # i번째부터 여태까지 확인한 패턴이 동일한 지 비교해야 함
            if lst[i:i + (len(new_lst))] == new_lst: # 같아진 시점부터 저장한 만큼의 길이동안 비교해야함
                ans = len(new_lst) # 만약 저장한 부분과 같으면 그게 패턴임
                break
        # 중요 !!
        new_lst.append(lst[i]) # else 쓰면 안 돼 !!!
        # 검사 하고 나왔을 때도 아니라면 append 해야 됨

    print(f'#{tc} {ans}')

# 하나씩 저장하다가 0번이랑 같은 문자를 만나면
# KOREA K 등장 !! = > 검사 시작
# K가 나랑 같은 문자열 이거나 그냥 패턴의 연장일수도 있음
# 만난 K가 나와 똑같이 KOREA를 가지는 지 확인
# K를 만나기 전의 길이랑 만난 K의 길이 동일하게 확인

# 근데  ?? 이 두개가 같다 ????? 그럼 패턴 인 거 쥐 ~
# 그럼 그 때까지 비교한 값 // 2 하면 마디 길이 아님 ?
# 새로운 배열에 넣고 그 새로운 배열의 길이 / 2 해보자




