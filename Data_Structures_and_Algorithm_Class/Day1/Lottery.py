## 내 답
import random

count = int(input('로또 복권을 몇 장 구입 하실래요? '))

if count != 0:
    for i in range(count):
        final_list = []
        while (len(final_list) != 6):
            num1 = random.randint(0, 45)     #randrange 는 0부터 44까지다!!
            if len(final_list) != 6  & num1 not in final_list:
                final_list.append(num1)
        print(sorted(final_list))

# 내 코드 단점
# random 모듈 안 함수 사용 잘못함
# 조건을 읽기 힘듦



# 교수님 수업자료

import random

num = int(input('로또 복권을 몇 장 구입 하실래요? '))

table = []

for i in range(num):
    sList = []
    while len(sList) <= 6:
        temp = random.randrange(1, 45)
        if temp in sList:
            continue
        sList.append(temp)
        sList.sort()
        table.append(sList)

for i in range(len(table)):
    print(table[i])
    
### 다중 리스트를 사용하여 리스트 별로 출력한 다는 것이 신박함
### 예외 처리가 안되어 있다는 것이 단점 
