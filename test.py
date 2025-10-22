def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before function")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper


@my_decorator
def say_hi(name):
    print(f"Hello {name}")


say_hi("Vlad")
