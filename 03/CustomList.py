from itertools import zip_longest


class CustomList(list):

    def __add__(self, other):
        return CustomList([sum(i) for i in zip_longest(self,
                                                       other,
                                                       fillvalue=0)])

    def __sub__(self, other):
        return CustomList([sum(i) for i in
                           zip_longest(self,
                                       [-number for number in other],
                                       fillvalue=0)])

    def __radd__(self, other):
        return CustomList([sum(i) for i in zip_longest(other,
                                                       self,
                                                       fillvalue=0)])

    def __rsub__(self, other):
        return CustomList([sum(i) for i in
                           zip_longest(other,
                                       [-number for number in self],
                                       fillvalue=0)])

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __repr__(self):
        return "CustomList(" + super().__repr__() + ")"

    def __str__(self):
        return super().__str__() + f" sum = {sum(self)};"


def main():
    if __name__ == '__main__':
        sub = CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])
        add = CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])
        print(f"Only customs\nADD = {add}\n"
              f"SUB = {sub}\n")
        add_list = CustomList([5, 1, 3, 7]) + [1, 2, 7]
        sub_list = CustomList([5, 1, 3, 7]) - [1, 2, 7]
        print(f"Custom +- list\nADD = {add_list}\n"
              f"SUB = {sub_list}\n")
        add_list_r = [1, 2, 7] + CustomList([5, 1, 3, 7])
        sub_list_r = [1, 2, 7] - CustomList([5, 1, 3, 7])
        print(f"List +- custom\nADD = {add_list_r}\n"
              f"SUB = {sub_list_r}\n")
        return "end of main"
    return "just end"


main()
