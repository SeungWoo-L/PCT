# 연습 문제 1
# 피보나치 수열 : 성능 평가

# 비 재귀적 피보나치 수열

def Fibonacci_Non(num:int):
    temp = 1  # 첫 번째 피보나치 수
    temp2 = 1  # 두 번째 피보나치 수

    if num == 1:
        print(temp)
        return
    elif num == 2:
        print(temp, end="\t")
        print(temp2)
        return

    print(temp, end="\t")  # 첫 번째 수 출력
    print(temp2, end="\t")  # 두 번째 수 출력

    for i in range(2, num):  # num>=3 피보나치 수열을 계산 (첫 두 수는 출력됨)
        answer = temp + temp2
        if i % 5 == 0:
          print() # 5개 출력 후 줄 바꿈
        print(answer, end="\t")  # 피보나치 수 출력
        temp = temp2  # 현재 두 번째 수를 첫 번째 수로 업데이트
        temp2 = answer  # 계산된 수를 두 번째 수로 업데이트

    print() #  줄바꿈

# 재귀적 피보나치 수열

def Fibonacci_Rec(num:int):
  if num <= 1:
    return num
  else:
    return Fibonacci_Rec(num-1) + Fibonacci_Rec(num-2)

# 재귀적 피보나치 수열 출력
def Fibonacci_Rec_Print(num:int):
  for i in range(1, num+1):
    answer = Fibonacci_Rec(i)
    if (i-1) % 5 == 0 and i > 1: # 5개 출력 후 줄 바꿈
      print()
    print(answer, end='\t')
  print()

if __name__ == '__main__':
  import time

  num = int(input('몇 번째 수열까지 출력할까요: '))

  start_time = time.time() # 비 재귀적 피보나치 함수 시작시간
  Fibonacci_Non(num)
  non_duration = time.time() - start_time # 비 재귀적 피보나치 함수 수행시간 계산
  print() # 줄 바꿈
  print(f'비 재귀적 함수 수행시간 : {non_duration}초')

  rec_start_time = time.time() # 재귀적 피보나치 함수 시작시간
  Fibonacci_Rec_Print(num)
  rec_duration = time.time() - rec_start_time # 재귀적 피보나치 함수 수행시간 계산
  print()
  print(f'재귀적 함수 수행시간 : {rec_duration}초')




