from array import array

import tracemalloc

tracemalloc.start()

myarray = array('I', range(100_000_000))

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
tracemalloc.stop()
