# 연습문제 3-1
# 계승(Factorial) 구하기 : BaekJoon 10872
# 비 재귀적 용법 사용

def factorial(N):
    if N == 0:
        return 1
    result = 1
    for i in range(2, N+1):
        result *= i
    return result

if __name__ == '__main__':
    N = int(input())
    print(f'{factorial(N)}')
    
    
# 연습문제 3-2
# 계승(Factorial) 구하기 : BaekJoon 27433
# 재귀적 용법 사용
def Factorial(N):
    if N == 0:
        return 1
    return N * Factorial(N-1)

N = int(input())
print(f'{Factorial(N)}')


# 연습문제 3-3
# 계승(Factorial) 구하기 : BaekJoon 27434
# 반복문 사용
def Factorial(N):
    result = 1
    for i in range(2, N+1):
        result *= i
    return result

if __name__ == '__main__':
    N = int(input())
    print(f'{Factorial(N)}')