class CustomMeta(type):

    def __new__(mcs, name_cls, bases, dct):
        def _setattr(self, key, val):
            self.__dict__[f"custom_{key}"] = val

        changing_name = 'custom_'
        new_dct = {}
        for name, value in dct.items():
            if not (name.startswith('__') and name.endswith('__')):
                new_dct[changing_name + name] = value
            else:
                new_dct[name] = value

        cls = super().__new__(mcs, name_cls, bases, new_dct)
        cls.__setattr__ = _setattr
        return cls


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 'Line: ' + str(self)

    def __str__(self):
        return "Custom_by_metaclass"
