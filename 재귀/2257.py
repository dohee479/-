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








# def cal(i, result):
#     global ans
#     global tmp
#     if i == -1:
#         return 0
#
#     if chemical[i] == 'H':
#         if result != 0:
#             ans += result
#         cal(i-1, 1)
#
#     if chemical[i] == 'C':
#         if result != 0:
#             ans += result
#         cal(i-1, 12)
#
#     if chemical[i] == 'O':
#         if result != 0:
#             ans += result
#         cal(i-1, 16)
#
#     elif '1' <= chemical <= '9':
#         ans += (result*(chemical[i]-'0'))
#         cal(i-1, 0)
#
#     elif chemical[i] == '(':
#         ans += result
#         tmp = ans
#         cal(i-1, 0)
#
#     elif chemical[i] == ')':
#         t2 = ans + result
#         ans = tmp
#         cal(i-1, t2-tmp)
#
#
# chemical = input()
# chem = {'H': 1, 'C': 12, 'O': 16}
# ans = 0
# tmp = 0
# cal(len(chemical)-1, 0)


