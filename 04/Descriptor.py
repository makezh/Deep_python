class Integer:
    def __set_name__(self, owner, name) -> None:
        self.name = name

    def __get__(self, obj: 'Data', _):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj: 'Data', value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer.")
        obj.__dict__[self.name] = value

    def __delete__(self, obj: 'Data') -> None:
        if self.name not in obj.__dict__:
            raise AttributeError(self.name)
        del obj.__dict__[self.name]


class String:
    def __get__(self, obj: 'Data', _):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set_name__(self, owner, name) -> None:
        self.name = name

    def __set__(self, obj: 'Data', value):
        if not isinstance(value, str):
            raise TypeError(f"{self.name} must be a string.")
        obj.__dict__[self.name] = value

    def __delete__(self, obj: 'Data') -> None:
        if self.name not in obj.__dict__:
            raise AttributeError(self.name)
        del obj.__dict__[self.name]


class PositiveInteger:
    def __set_name__(self, owner, name) -> None:
        self.name = name

    def __get__(self, obj: 'Data', _):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj: 'Data', value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError(f"{self.name} must be a positive integer.")
        obj.__dict__[self.name] = value

    def __delete__(self, obj: 'Data') -> None:
        if self.name not in obj.__dict__:
            raise AttributeError(self.name)
        del obj.__dict__[self.name]


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num=1, name='base', price=1):
        self.num = num
        self.name = name
        self.price = price

    def __str__(self):
        return f'#{self.num}, name = {self.name}, price = {self.price}$'


def main():
    if __name__ == '__main__':
        data = Data()
        print(data)
        data.num = 10
        data.price = 135
        data.name = 'gift'
        print(data)
        return "end of main"
    return 'just end'

main()