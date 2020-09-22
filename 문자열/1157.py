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