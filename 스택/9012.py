# 괄호
import sys
sys.stdin = open('input.txt', 'r')


def check(target):
    stack = list()
    for i in range(len(target)):
        if target[i] == '(':
            stack.append(target[i])
        elif target[i] == ')':
            if len(stack) == 0:
                return False
            tmp = stack.pop()
            if target[i] == ')' and tmp == '(':
                continue
            return False
    if len(stack) > 0:
        return False
    return True


N = int(input())
for _ in range(N):
    word = input()
    if check(word):
        print("YES")
    else:
        print("NO")



