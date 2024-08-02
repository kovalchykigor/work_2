def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n", f"Func call '{func.__name__}' with arguments: 'args={args}, kwargs={kwargs}'")
        result = func(*args, **kwargs)
        print(f"Result of func '{func.__name__}' is: '{result}'", "\n")
        return result

    return wrapper


def error_decorator_for_generator(func):
    def wrapper(*args, **kwargs):
        try:
            generator = func(*args, **kwargs)
            while True:
                try:
                    yield next(generator)
                except StopIteration:
                    break
        except Exception as e:
            yield f"ERROR TYPE: {e}"

    return wrapper


def error_decorator_for_iterator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"ERROR TYPE: {e}"
    return wrapper