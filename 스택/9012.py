# 괄호
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for _ in range(N):
    word = input()
    stack = []
    for i in range(len(word)):
        if word[i] == '(':
            stack.append(word[i])
        elif word[i] == ')':
            if len(stack) == 0:
                if i == 0:
                    print(A)
                else:
                    print(A)
                    continue
            tmp = stack.pop()
            if word[i] == ')' and tmp == '(':
                continue
    if len(stack) == 0:
        print(B)
    else:
        print(A)



