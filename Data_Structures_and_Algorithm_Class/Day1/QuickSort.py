def quickSort(s, first:int, last:int):
    if (first >= last):
        return
    
    # 분할: 기준 값의 왼쪽(작은 값)과 오른쪽(큰 값) 부분 집합
    pivot,i = s[last], first        # pivot: 기준 값(S[last])
    for j in range(first, last):
        if(s[j] <= pivot):          # pivot: 기준 값: 마지막 원소
            s[i], s[j] = s[j],s[i]
            i += 1
    s[i],s[last] = s[last], s[i]    # 기준 값을 가운데로
    quickSort(s, first, i-1)        # 왼쪽 부분 정렬
    quickSort(s, i+1, last)         # 오른 쪽 부분 정렬
    
    
def selectionSort(sList):
    for i in range(len(sList)):
        smIndex = i
        for j in range(i, len(sList)):
            if sList[smIndex] > sList[j]:
                smIndex = j
                
        sList[smIndex], sList[i] = sList[i], sList[smIndex]
        # print(sList)


if __name__ == '__main__':
    import random
    sList = []
    while len(sList)<10:
        num = random.randint(0, 99)
        sList.append(num)
    
    print(f'정렬 전: {sList}')    
    selectionSort(sList)
    # bubbleSort(sList)
    # insertionSort(sList)
    # shellSort(sList)
    # quickSort(sList, 0, len(sList)-1)
    # mergeSort(sList, 0, len(sList)-1)
    # countingSort(sList)
    print(f'정렬 후: {sList}')