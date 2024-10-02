# 연습문제 4-2
# 수 정렬하기: BaekJoon 2751

import sys

input = sys.stdin.read

N, *numbers = map(int, input().split())

numbers.sort()
sys.stdout.write("\n".join(map(str, numbers)) + "\n")