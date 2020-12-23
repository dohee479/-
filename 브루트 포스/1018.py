# 체스판 다시 칠하기
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
result = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        start_w, start_b = 0, 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l - i - j) % 2:
                    if chess[k][l] == 'W':
                        start_w += 1
                    else:
                        start_b += 1
                else:
                    if chess[k][l] == 'B':
                        start_w += 1
                    else:
                        start_b += 1
        result = min(result, start_w, start_b)
print(result)








                    


                
    
    