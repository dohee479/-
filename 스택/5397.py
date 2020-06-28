# 키로거
import sys
sys.stdin = open('input.txt', 'r')

# 시간초과
# T = int(input())
# for t in range(T):
#     word = input()
#     result = []
#     stack = []
#     for w in word:
#         if w == '<':
#             if result:
#                 stack.insert(0, result.pop())
#         elif w == '>':
#             if stack:
#                 result.append(stack.pop(0))
#         elif w == '-':
#             if result:
#                 result.pop()
#         else:
#             result.append(w)
#     result.extend(stack)
#     print(''.join(result))

T = int(input())
for t in range(T):
    word = input()
    result = []
    stack = []
    for w in word:
        if w == '<':
            if result:
                stack.append(result.pop())
        elif w == '>':
            if stack:
                result.append(stack.pop())
        elif w == '-':
            if result:
                result.pop()
        else:
            result.append(w)
    result.extend(reversed(stack))
    print(''.join(result))

