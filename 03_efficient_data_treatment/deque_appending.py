import timeit
from collections import deque

myqueue = deque(range(100_000_000))


def test():
    for _ in range(10):
        myqueue.append(1)
        myqueue.popleft()
        len(myqueue)


measured_time = int(timeit.timeit(test, number=1) * 1000000)
print(f'Time is {measured_time} us')
