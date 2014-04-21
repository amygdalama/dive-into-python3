from functools import reduce

def fib_generator(max_num):
    a = 0
    b = 1
    while b <= max_num:
        yield b
        a, b = b, a+b

[f for f in fib_generator(100)]

def fib_recursion(max_num, series=None):
    if not series:
        series = [1, 1]
    if series[-1] > max_num:
        return series[:-1]
    else:
        series.append(series[-1] + series[-2])
        return fib_recursion(max_num, series)

def fib_while(max_num, series=[1,1]):
    while series[-1] < max_num:
        series.append(series[-1] + series[-2])
    return series[:-1]

def fib_reduce(max_index, series=[1,1]):
    return reduce(lambda a, x: a + [a[-1] + a[-2]], range(max_index), series)

def fib(x):
    if x < 2:
        return x
    else:
        return fib(x-1) + fib(x-2)

def fib_map(max_index):
    return list(map(fib, range(1, max_index+1)))

def fib_list_comprehension(max_index):
    return [fib(x) for x in range(1, max_index+1)]