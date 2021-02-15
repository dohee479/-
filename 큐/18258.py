# 큐 2
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
queue = []
front = 0
rear = -1
for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
        rear += 1

    elif cmd[0] == 'pop':
        if rear >= front:
            print(queue[front])
            front += 1
        else:
            print(-1)

    elif cmd[0] == 'size':
        print(rear - front + 1)

    elif cmd[0] == 'empty':
        if rear - front + 1:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'front':
        if rear >= front:
            print(queue[front])
        else:
            print(-1)

    elif cmd[0] == 'back':
        if rear >= front:
            print(queue[rear])
        else:
            print(-1)