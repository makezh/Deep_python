class ProfileDeco:
    def __init__(self, function):
        self.func = function
        self.func.calls = 0

    def __call__(self, *args, **kwargs):
        self.func.calls += 1
        return self.func(*args, **kwargs)

    def print_stat(self):
        print(f"{self.func.__name__}() вызвана {self.func.calls} раз")


@ProfileDeco
def add(first, second):
    return first + second


@ProfileDeco
def sub(first, second):
    return first - second


def main():
    add(1, 2)
    add(4, 5)
    sub(4, 2)
    add(3, 6)

    add.print_stat()
    sub.print_stat()


if __name__ == "__main__":
    main()
