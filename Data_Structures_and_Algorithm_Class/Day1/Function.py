def MAXMIN(sList):
    if sList == [] :
        return None, None
    max, min = sList[0], sList[0]
    for i in range(0, len(sList)) :
        if sList[i] > max: max = sList[i]
        if sList[i] < min: min = sList[i]
    return max, min

sList = []
print('임의의 정수를 입력하세요...')
i = 0
while True:
    num = input(f'sList[{i}] : ')
    if num == 'end' or num == '':
        break
    sList.append(int(num))
    i+=1
    
max, min = MAXMIN(sList) 
print(f'최댓값: {max}, 최솟값: {min}')
 
        