def log_decorator(func):
    def wrapper():
        print("print avant la fonction")
        func()
        print("print après la fonction")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
