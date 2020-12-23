# 한수
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
cnt = 0
for number in range(1, N+1):
    num = str(number)
    if len(str(num)) <= 2:
        cnt += 1
    else:
        compare = int(num[1]) - int(num[0])
        check = 0
        for i in range(1, len(num)-1):
            if int(num[i + 1])-int(num[i]) == compare:
                check += 1
        if check == len(num) - 2:
            cnt += 1
print(cnt)



