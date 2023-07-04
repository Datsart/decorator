def type_logger(func):
    def wrapper(*args, **kwargs):
        # print(args, 'args')
        # print(kwargs, 'kwargs')
        result = func(*args, **kwargs)
        return f"{args[0]}: {type(args[0])}"

    return wrapper


@type_logger
def func_1(data):
    return data ** 3


data = 5
print(func_1(data))
