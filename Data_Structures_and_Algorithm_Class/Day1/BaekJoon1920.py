# 연습문제 6
# 수 찾기 BaekJoon 1920

N = int(input())
NList = set(map(int, input().split()))
# set을 사용하여 중복된 값을 제거함과 동시에 해시 테이블을 이용하여 탐색 시간을 줄임

M = int(input())
MList = list(map(int, input().split()))

for i in MList:
    if i in NList:
        print(1)
    else:
        print(0)