from typing import Tuple


def get_sum(a: int, b: int = 2, c: int = 3, *args, **kwargs) -> Tuple[int, int]:
    sum = a+b+c
    diferenta = a-b-c
    print(args)
    print(kwargs, type(kwargs))
    for i in kwargs.values():
        sum += i
        dif -= i
    return sum, diferenta


var1, var2, = get_sum(1, 4, 4, 4, d=3, e=4, f=5)
print(var1, var2)
