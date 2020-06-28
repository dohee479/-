# 일곱 난쟁이
import sys
sys.stdin = open('input.txt', 'r')


def DFS(m):
    if len(result) == 7:
        if sum(result) != 100:
            return
        else:
            for i in range(len(result)):
                print(result[i])
            print()
            sys.exit()
            return

    for i in range(m):
        if visited[i] == 1:
            continue
        result.append(hobit[i])
        for j in range(i+1):
            visited[j] = 1
        DFS(m)
        for j in range(i, m):
            visited[j] = 0
        result.pop()

hobit = []
for _ in range(9):
    num = int(input())
    hobit.append(num)
    hobit.sort()
visited = [0] * 9
result = []
DFS(len(hobit))


def DFS(m, sol):
    if len(result) == 7 and sum(result) == 100:
        a = result.copy()
        sol.append(a)
        # sol.append(result)
        return

    for i in range(m):
        if visited[i] == 1:
            continue
        result.append(hobit[i])
        for j in range(i+1):
            visited[j] = 1
        DFS(m, sol)
        for j in range(i, m):
            visited[j] = 0
        result.pop()

hobit = []
for _ in range(9):
    hobit.append(int(input()))
hobit.sort()
visited = [0] * 9
result = []
sol = []
DFS(len(hobit), sol)
print(sol)
for i in sol[0]:
    print(i)


