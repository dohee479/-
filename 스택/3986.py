# 좋은 단어
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
cnt = 0
for n in range(N):
    word = input()
    stack = []
    for i in range(len(word)):
        if len(stack) == 0:
            stack.append(word[i])
            continue
        else:
            if word[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(word[i])
    if len(stack) == 0:
        cnt += 1
print(cnt)

