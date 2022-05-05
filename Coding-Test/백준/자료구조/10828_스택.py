import sys
from typing import List
from pprint import pprint

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

stack = []

for i in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        if len(stack) > 0:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    



