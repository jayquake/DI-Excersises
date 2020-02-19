import time
import math


def decorator(func):
    def wrapper (*args,**kwargs):
        print(f"Running{func}")
        func()
        print("Done")

    return wrapper

@decorator
def talk():
    print("speech")

def timeit(func):
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        output =func(*args,**kwargs)
        end = time.perf_counter() - start
        round(end)
        print(f"function took: {end} seconds")
        return output
    return wrapper
@timeit
def compute(power):
    return 2**power

compute(323044444)
