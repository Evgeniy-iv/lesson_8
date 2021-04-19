def type_logger(func):
    def wrapper(*args) :
        type_el = (f'{el}: {type(el)}' for el in args)
        print(*type_el)
        result = func(*args)
        return result
    return wrapper

@type_logger
def volume(a, b, c):
    return a * b * c

print(volume(4, 6, 5))
