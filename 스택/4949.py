# 균형잡힌 세상
import sys
sys.stdin = open('input.txt', 'r')

while True:
    string = input()
    if string == ".":
        break
    stack = []
    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)
        elif s == "[":
            stack.append(s)
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(s)
    if not stack:
        print("yes")
    else:
        print("no")
