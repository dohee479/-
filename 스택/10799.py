# 쇠막대기
import sys
sys.stdin = open('input.txt', 'r')

word = input()
stack = []
cnt = 0
stack = [word[0]]
for i in range(1, len(word)):
    if word[i] == '(':
        stack.append(word[i])
    else:
        stack.pop()
        if word[i - 1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)