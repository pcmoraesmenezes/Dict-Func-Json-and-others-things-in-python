def soma_decorator(func):
    def wrapper(x, y):
        result = func(x, y)
        return result

    return wrapper

@soma_decorator
def soma(x, y):
    return x + y

print(soma(2, 3))
