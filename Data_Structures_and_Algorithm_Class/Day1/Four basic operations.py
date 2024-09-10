num1, op, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
answer = None
match op:
    case  '+' : answer = num1 + num2 
    case  '-' : answer = num1 - num2 
    case  '*' : answer = num1 * num2 
    case  '/' : 
        try:
            answer = num1 / num2
        except ZeroDivisionError as e: print(f'오류: {e}')
                
    case default: 
        answer = None
        print('지원하지 않는 연산자입니다.') 
    
if answer is not None:
    print (f'{num1} {op} {num2} = {answer}')


###
# Raise(사용자 정의 예외 사용 시)
###
num1, op, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
answer = None
match op:
    case  '+' : answer = num1 + num2 
    case  '-' : answer = num1 - num2 
    case  '*' : answer = num1 * num2 
    case  '/' : 
        if num2 == 0:
            raise Exception('0 으로는 나눌 수 없습니다!!!')
        else:
            answer = num1 / num2
    case default: 
        answer = None
        print('지원하지 않는 연산자입니다.') 
    
if answer is not None:
    answer = int(answer)
    print (f'{num1} {op} {num2} = {answer}')
