# 연산자 끼워넣기
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def backtrack(index, result):
    global min_result, max_result
    if index == len(A) - 1:
        if result < min_result:
            min_result = result
        if result > max_result:
            max_result = result
        return

    for i in range(len(operator)):
        if operator[i]:
            if i == 0:
                operator[i] -= 1
                backtrack(index + 1, result + A[index + 1])
                operator[i] += 1
            elif i == 1:
                operator[i] -= 1
                backtrack(index + 1, result - A[index+1])
                operator[i] += 1
            elif i == 2:
                operator[i] -= 1
                backtrack(index + 1, result * A[index+1])
                operator[i] += 1
            else:
                if result < 0:
                    result = abs(result)
                    operator[i] -= 1
                    backtrack(index + 1, -(result // A[index + 1]))
                    operator[i] += 1
                else:
                    operator[i] -= 1
                    backtrack(index + 1, result // A[index + 1])
                    operator[i] += 1


N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_result = 100000000000
max_result = -100000000000
backtrack(0, A[0])
print(max_result)
print(min_result)
