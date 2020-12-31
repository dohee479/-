# 통계학
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
number = [int(input()) for _ in range(N)]
number.sort()
# 숫자들의 빈도수들 딕셔너리 형태로 저장, 음수값도 존재해서 리스트로 하지 않음
count = {}
for num in number:
    if count.get(num):
        count[num] += 1
    else:
        count[num] = 1
# 산술 평균 후 반올림
print(round(sum(number) / N))
# 중앙값
print(number[N // 2])
# 최빈값
max_count = [key for key, value in count.items() if value == max(count.values())]
if len(max_count) > 1:
    print(max_count[1])
else:
    print(max_count[0])
# 범위 (최댓값과 최솟값의 차이)
print(max(number) - min(number))


# 시간초과
# 최빈값
# 중복되는 수를 다 볼필요 없다. 중복제거후 정렬하여 개수를 구한다
# O(n^2) 예상
frequency = []
for num in sorted(set(number)):
    frequency.append(number.count(num))
# 최빈값이 여러개일 경우가 존재, 그 값들을 모아 두번째 값을 뽑아준다.
max_cnt = [i for i, value in enumerate(frequency) if value == max(frequency)]
# print(max_cnt[1])
