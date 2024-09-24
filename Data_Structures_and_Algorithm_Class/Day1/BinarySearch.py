#비 재귀적 용법
def binarySearch(sList, first:int, last:int, key:int):
    while(first<=last):
        mid = (first + last) // 2
        
        if key == sList[mid]: return mid
        elif key < sList[mid]: last = mid-1
        elif key > sList[mid]: first = mid+1
          
# 재귀적 용법
def binarySearch(sList, first:int, last:int, key:int):
    if first > last:
        return None
    
    mid = (first + last) // 2
    
    if sList[mid] == key: return mid
    elif sList[mid] < key:index = binarySearch(sList,mid+1,last,key)
    elif sList[mid] > key:index = binarySearch(sList,first,mid-1,key)
    return index
    
if __name__ == '__main__' :
    sList = [5, 9, 13, 17, 21, 28, 37, 46, 55, 88]
    print(f'원시 데이터: {sList}')
    while True :
        key = int(input('검색 데이터 입력(검색 종료: 0 ): '))
        if key == 0 : break
    
        index = binarySearch(sList, 0, len(sList)-1, key)
        if index == None:print('없다고!!!')
        else:print(f'검색된 데이터:{index+1}번째, {sList[index]}')

