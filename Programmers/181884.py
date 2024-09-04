# n보다 커질때까지 더하기

#python 1
def solution(numbers, n):
    answer = 0
    while True:
        for i in numbers:
            answer += i
            if answer > n:
                return answer
#