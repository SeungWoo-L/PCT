def countingSort(sList):
    k = max(sList)  # 최대값을 기준으로 배열 크기 결정
    C = [0 for _ in range(k+1)]  # 카운팅 배열 초기화
    
    # 각 숫자의 출현 횟수 계산
    for i in range(len(sList)): 
        C[sList[i]] += 1
    
    # 누적 합 계산
    for j in range(1, k+1):  
        C[j] += C[j-1]
    
    # 정렬된 결과를 저장할 배열 초기화
    B = [0 for _ in range(len(sList))]  
    
    # 입력 배열을 역순으로 순회하며 결과 배열에 정렬된 값을 채움
    for i in range(len(sList)-1, -1, -1):
        B[C[sList[i]]-1] = sList[i]
        C[sList[i]] -= 1
    
    # 원본 리스트에 정렬된 결과 복사 (while문 사용)
    i, t = 0, 0  # i는 sList의 인덱스, t는 B의 인덱스
    while i < len(B):
        sList[i] = B[t]
        t += 1
        i += 1
            
if __name__ == '__main__':
    import random
    sList = []
    while len(sList)<10:
        num = random.randint(0, 99)
        sList.append(num)
    
    print(f'정렬 전: {sList}')    
    # selectionSort(sList)
    # bubbleSort(sList)
    # insertionSort(sList)
    # shellSort(sList)
    # quickSort(sList, 0, len(sList)-1)
    # mergeSort(sList, 0, len(sList)-1)
    countingSort(sList)
    print(f'정렬 후: {sList}')