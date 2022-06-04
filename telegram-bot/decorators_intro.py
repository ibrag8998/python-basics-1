import time


def time_it(function):
    def wrapper():
        start = time.time()
        rv = function()
        end = time.time()
        print(f"`{function.__name__}()` time took: {end - start} s")
        return rv

    return wrapper


@time_it
def f():
    i = 0
    while i < 35_000_000:
        i += 1


@time_it
def g():
    i = 27_000_000
    while i > 0:
        i -= 1


f()
g()
