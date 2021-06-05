import timeit

myqueue = list(range(100_000_000))


def test():
    for _ in range(10):
        myqueue.append(1)
        myqueue.pop(0)
        len(myqueue)


measured_time = int(timeit.timeit(test, number=1) * 1000000)
print(f'Time is {measured_time} us')
