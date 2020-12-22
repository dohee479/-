# 단어 공부
import sys
sys.stdin = open('input.txt', 'r')

text = list(input().upper())
compare = list(set(text))
count_text = [0] * len(compare)
for i in range(len(compare)):
    count_text[i] = text.count(compare[i])
if count_text.count(max(count_text)) > 1:
    print('?')
else:
    print(compare[count_text.index(max(count_text))])


text = input().upper()
alpha = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
for i in text:
    alpha[i] += 1
max_value = 0
answer = ''
for i in alpha:
    if max_value < alpha[i]:
        max_value = alpha[i]
        answer = i
    elif max_value == alpha[i]:
        answer += i
if len(answer) > 1:
    print('?')
else:
    print(answer)


text = input().upper()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for i in alpha:
    result.append(text.count(i))
if result.count(max(result)) > 1:
    print("?")
else:
    print(alpha[result.index(max(result))])


