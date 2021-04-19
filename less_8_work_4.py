def val_checker(valid):
    def wrapper(func):
        def validator(*args):
            result = func(*args) if valid(*args) else ValueError(f'Неверное значение: {args}')
            return result
        return validator
    return wrapper

@val_checker(lambda x: x > 0)
def calc_cube(x) :
    return x ** 3
print(calc_cube(-7))
