# 덱
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
dequeue = []
front = 0
rear = -1
for _ in range(N):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'push_front':
        if not front:
            rear += 1
            dequeue[0:0] = [cmd[1]]
        else:
            dequeue[front:front] = [cmd[1]]
            rear += 1

    elif cmd[0] == 'push_back':
        dequeue.append(cmd[1])
        rear += 1

    elif cmd[0] == 'pop_front':
        if rear >= front:
            print(dequeue[front])
            front += 1
            if front > rear:
                rear = front - 1
        else:
            print(-1)

    elif cmd[0] == 'pop_back':
        if rear >= front:
            print(dequeue.pop())
            rear -= 1
            if front > rear:
                rear = front -1
        else:
            print(-1)

    elif cmd[0] == 'size':
        if rear >= front:
            print(rear - front + 1)
        else:
            print(0)

    elif cmd[0] == 'empty':
        if rear >= front:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'front':
        if rear >= front:
            print(dequeue[front])
        else:
            print(-1)

    elif cmd[0] == 'back':
        if rear >= front:
            print(dequeue[rear])
        else:
            print(-1)
