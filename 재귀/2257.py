# 화학식량
import sys
sys.stdin = open('input.txt', 'r')

word = input()
chem = {'H': 1, 'C': 12, 'O': 16}
stack = []
for i in range(len(word)):
    if word[i] == '(':
        stack.append(word[i])
    elif word[i] == ')':
        result = 0
        semi_result = stack.pop()
        while semi_result != '(':
            result += semi_result
            semi_result = stack.pop()
        stack.append(result)
    elif '1' <= word[i] <= '9':
        stack.append(stack.pop() * int(word[i]))
    else:
        stack.append(chem[word[i]])

print(sum(stack))










