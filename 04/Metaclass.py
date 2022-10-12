class CustomMeta(type):
    def __new__(cls, name_cls, bases, dct):
        changing_name = 'custom_'
        new_dct = {}
        for name, value in dct.items():
            if not name.startswith('__'):
                new_dct[changing_name + name] = value
            else:
                new_dct[name] = value

        return super(CustomMeta, cls).__new__(cls, name_cls, bases, new_dct)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 'Line: ' + str(self)

    def __str__(self):
        return "Custom_by_metaclass"

    def __setattr__(self, key, value):
        self.__dict__[f"custom_{key}"] = value
