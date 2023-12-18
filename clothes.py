from time import perf_counter
from collections import defaultdict
from numpy.random import randint, seed


def closeness(lst, depth=0):
    step = defaultdict(list)
    for i in lst:
        if len(a[i]) > depth:
            step[a[i][depth]].append(i)
    return sum(len(x) * (len(x) - 1) // 2 + closeness(x, depth + 1) for x in step.values() if len(x) > 1)


n, k = 10000, 30000
seed(24)
a = randint(1, 11, (n, k))
start = perf_counter()
print(f'Близость {closeness(list(range(n)))}')
print(f'Время расчета {perf_counter() - start:.3f}c')
