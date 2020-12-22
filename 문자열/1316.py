# 그룹 단어 체커
import sys
sys.stdin = open('input.txt', 'r')


def check():
    alpha = {'A': -1, 'B': -1, 'C': -1, 'D': -1, 'E': -1, 'F': -1, 'G': -1, 'H': -1, 'I': -1, 'J': -1, 'K': -1, 'L': -1,
             'M': -1, 'N': -1, 'O': -1, 'P': -1, 'Q': -1, 'R': -1, 'S': -1, 'T': -1, 'U': -1, 'V': -1, 'W': -1, 'X': -1,
             'Y': -1, 'Z': -1}

    for i, value in enumerate(word):
        if alpha[value] != -1:
            if abs(i - alpha[value]) > 1:
                return 0
            else:
                alpha[value] = i
        else:
            alpha[value] = i
    return 1


N = int(input())
cnt = 0
for _ in range(N):
    word = input().upper()
    cnt += check()
print(cnt)

result = 0
for i in range(int(input())):
    word = input()
    print(list(word))
    print(sorted(word, key=word.find))
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)


