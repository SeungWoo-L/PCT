# 연습문제 4-1
# 수 정렬하기: BaekJoon 2750

import sys

N = int(sys.stdin.readline())
List = [int(sys.stdin.readline()) for i in range(N)]
nList = sorted(List)

for i in range(N):
    print(nList[i])