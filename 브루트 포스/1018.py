# 체스판 다시 칠하기
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
result = float('inf')
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for k in range(i, i+7):
            for l in range(j, j+7):
                if 
                if j % 2:
                    if k == i and l == j:
                        if chess[k][l] == 'W':
                            if l % 2:
                                if chess[k][l] != 'W':
                                    cnt += 1
                            else:
                                if chess[k][l] != 'B':
                                    cnt += 1
                        else:
                            if l % 2:
                                if chess[k][l] != 'B':
                                    cnt += 1
                            else:
                                if chess[k][l] != 'W':
                                    cnt += 1

                else:
                    if k == i and l == j:
                        if chess[k][l] == 'W':
                            if l % 2:
                                if chess[k][l] != 'B':
                                    cnt += 1
                            else:
                                if chess[k][l] != 'w':
                                    cnt += 1
                        else:
                            if l % 2:
                                if chess[k][l] != 'W':
                                    cnt += 1
                            else:
                                if chess[k][l] != 'B':
                                    cnt += 1
        result = min(result, cnt)
print(result)








                    


                
    
    