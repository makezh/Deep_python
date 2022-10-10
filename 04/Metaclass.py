class CustomMeta(type):
    def __new__(mcs, name, bases, dct):
        changing_name = 'custom_'
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        changed_dct = dict((changing_name + name, value) for name, value in attrs)

        return super(CustomMeta, mcs).__new__(mcs, name, bases, changed_dct)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return self.__dir__()

    def __str__(self):
        return "Custom_by_metaclass"

    def __getattribute__(self, item):
        print(f"getattribute {item}")
        return type.__getattribute__(item)

    def __setattr__(self, key, value):
        print(f"setattr {key} = {value}")
        return type.__setattr__("custom" + key, value)

    def __delattr__(self, item):
        print(f"delattr {item}")
        return type.__delattr__(item)

    def __getattr__(self, item):
        print(f"getattr {item}")
        return type.__getattr__(item)


inst = CustomClass()
inst.__setattr__("p", "q")
print(inst.__dict__.items())
print(inst.__dir__())
print(hasattr(inst, 'custom_val'))
'''
inst.custom_x == 50
inst.custom_val == 99
inst.custom_line() == 100
CustomClass.custom_x == 50
str(inst) == "Custom_by_metaclass"

inst.dynamic = "added later"
inst.custom_dynamic == "added later"
inst.dynamic  # ошибка

inst.x  # ошибка
inst.val  # ошибка
inst.line()  # ошибка
inst.yyy  # ошибка
CustomClass.x  # ошибка'''
