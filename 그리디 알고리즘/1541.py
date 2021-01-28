import sys
sys.stdin = open('input.txt', 'r')

# - 를 기준으로 split를 하면 +로 이루어지는 묶어지는 부분들이 존재한다.
expression = sys.stdin.readline().rstrip().split('-')
number = []
answer = 0
# + 로 묶어진 부분을 split하여 더해준다.
for i in expression:
    plus = 0
    for j in i.split('+'):
        plus += int(j)
    number.append(plus)
# 처음 값만 더해주고 나머지만 빼준다.
for i in range(len(number)):
    if i:
        answer -= number[i]
    else:
        answer += number[i]
print(answer)
