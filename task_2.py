from random import randint


def decorator(mode=0):
    def _decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args)
            modification = func.__name__
            if mode == 0:
                modification = f'{modification}: {type(result)}'
            if mode == 1:
                modification = f'{modification}: {result + 10}'
            if mode == 2:
                modification = f'-------------------\n{modification} {result}\n-------------------'
            return modification

        return wrapper

    return _decorator


@decorator(2)
# @decorator(1)
# @decorator(0)
def random_numbers(num1, num2):
    return randint(num1, num2)


print(random_numbers(1, 10))
