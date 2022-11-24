def profile_deco(func):
    def helper(*args, **kwargs):
        helper.print_stat += 1
        return func(*args, **kwargs)

    helper.print_stat = 0
    helper.__name__ = func.__name__
    return helper


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


add(1, 2)
add(4, 5)

print(add.print_stat)
