#!/usr/bin/python3
import os
import random
import time
import sys

def fork():
    kid = os.fork()
    if kid > 0:
        print(f'Parent[{os.getpid()}]: I ran children process with PID {kid}')
    else:
        num = random.randint(5, 10)
        os.execl('./child.py', './child.py', str(num))

    return kid


n = int(sys.argv[1])

for i in range(n):
    child = fork()

while n > 0:
    child_pid, status = os.wait()
    if status != 0:
        child = fork()
    else:
        print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.')
        n = n - 1

os._exit(os.EX_OK)

