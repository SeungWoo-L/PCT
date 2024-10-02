import random

# 이진 검색 함수
def binarySearch(sList, first:int, last:int, key:int):
    while first <= last:
        mid = (first + last) // 2  # 중간 인덱스 계산
        if sList[mid] == key:
            return mid  # 값을 찾으면 해당 인덱스 반환
        elif sList[mid] < key:
            first = mid + 1  # 검색 범위를 오른쪽으로 좁힘
        else:
            last = mid - 1  # 검색 범위를 왼쪽으로 좁힘
    return -1  # 값을 찾지 못하면 -1 반환

# 병합 정렬 함수
def merge_sort(datas):
    if len(datas) <= 1:
        return datas

    mid = len(datas) // 2
    left_half = merge_sort(datas[:mid])  # 왼쪽 절반 재귀적 정렬
    right_half = merge_sort(datas[mid:])  # 오른쪽 절반 재귀적 정렬

    # 병합 과정
    result = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    # 남은 요소를 추가
    result.extend(left_half[i:])
    result.extend(right_half[j:])

    return result

# 메인 함수
if __name__ == '__main__':
    # 1에서 100 사이의 임의의 10개 숫자를 리스트로 생성
    data = [random.randint(1, 100) for i in range(10)]

    # 병합 정렬 수행
    data = merge_sort(data)

    # 정렬된 데이터를 출력
    print(f'원시데이터 : {data}')

    while True:
        # 검색할 데이터를 입력받음 (0을 입력하면 종료)
        num = int(input('검색 데이터 입력(검색 종료: 0 ): '))

        if num == 0:
            break

        # 이진 검색 수행
        result = binarySearch(data, 0, len(data) - 1, num)

        if result != -1:
            # 데이터를 찾으면 해당 위치와 함께 출력
            print(f'검색된 데이터: {result + 1}번째 {num}')
        else:
            # 데이터를 찾지 못하면 '없다고!!!' 출력
            print('없다고!!!')
