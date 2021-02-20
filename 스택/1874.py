# 스택 수열
import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
seq = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
stack = []
answer = []
possible = True
i = 1
j = 0
while j < n:
    if not stack:
        stack.append(i)
        answer.append("+")
        i += 1
    if i <= n:
        if stack[-1] == seq[j]:
            stack.pop()
            answer.append("-")
            j += 1
            continue

        if stack[-1] != seq[j]:
            if i > stack[-1]:
                stack.append(i)
                answer.append("+")
            else:
                print("NO")
                possible = False
                break
        i += 1
    else:
        if stack[-1] == seq[j]:
            stack.pop()
            answer.append("-")
            j += 1
            continue

        if stack[-1] != seq[j]:
            if stack[-1] > seq[j]:
                print("NO")
                possible = False
                break
if possible:
    print("\n".join(answer))







