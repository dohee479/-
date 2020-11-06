# 그룹 단어 체커
import sys
sys.stdin = open('input.txt', 'r')

alpha = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
N = int(input())
cnt = 0
for _ in range(N):
    word = input().upper()
    for i in range(len(word)):
        for j in range(len(word)):
            if word[i] == word[j]:
                if abs(i - j) > 1:
                    break
print(cnt)


