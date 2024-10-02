# 연습문제 5
# 두 배열의 원소 교체: 국제 알고리즘 대회

# n: 배열의 크기, k: 최대 교체 횟수 입력
n, k = map(int, input().split())

# 배열 a와 b의 원소 입력받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 배열 a는 오름차순으로 정렬
a.sort()

# 배열 b는 내림차순으로 정렬
b.sort(reverse=True)

# 최대 k번의 교체 작업 수행
for i in range(k):
    # a의 원소가 b의 원소보다 작을 경우에만 교체
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break  # 만약 a[i]가 b[i]보다 크거나 같으면 교체 종료

# 배열 a의 모든 원소의 합을 출력
print(sum(a))
