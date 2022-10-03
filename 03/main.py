from itertools import zip_longest


class CustomList(list):
    def __init__(self, lst=None):
        super().__init__()
        if lst is not None:
            self.list = list(lst)
        else:
            self.list = []

    def __add__(self, other):
        if isinstance(other, CustomList):
            return CustomList([sum(i) for i in zip_longest(self.list,
                                                           other.list,
                                                           fillvalue=0)])
        return CustomList([sum(i) for i in zip_longest(self.list,
                                                       other,
                                                       fillvalue=0)])

    def __sub__(self, other):
        if isinstance(other, CustomList):
            return CustomList([sum(i) for i in
                               zip_longest(self.list,
                                           [-number for number in other.list],
                                           fillvalue=0)])

        return CustomList([sum(i) for i in
                           zip_longest(self.list,
                                       [-number for number in other],
                                       fillvalue=0)])

    def __radd__(self, other):
        return CustomList([sum(i) for i in zip_longest(other,
                                                       self.list,
                                                       fillvalue=0)])

    def __rsub__(self, other):
        return CustomList([sum(i) for i in
                           zip_longest(other,
                                       [-number for number in self.list],
                                       fillvalue=0)])

    def __lt__(self, other):
        return sum(self.list) < sum(other.list)

    def __le__(self, other):
        return sum(self.list) <= sum(other.list)

    def __gt__(self, other):
        return sum(self.list) > sum(other.list)

    def __ge__(self, other):
        return sum(self.list) >= sum(other.list)

    def __eq__(self, other):
        return sum(self.list) == sum(other.list)

    def __ne__(self, other):
        return sum(self.list) != sum(other.list)

    def __len__(self):
        return len(self.list)

    def __repr__(self):
        return f'CustomList({self.list})'

    def __str__(self):
        return f'{self.list} sum = {sum(self.list)};'


def main():
    if __name__ == '__main__':
        sub = CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])
        add = CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])
        print("Only customs", add, sub, '', sep='\n')
        add_list = CustomList([5, 1, 3, 7]) + [1, 2, 7]
        sub_list = CustomList([5, 1, 3, 7]) - [1, 2, 7]
        print("Custom +- list", add_list, sub_list, '', sep='\n')
        add_list_r = [1, 2, 7] + CustomList([5, 1, 3, 7])
        sub_list_r = [1, 2, 7] - CustomList([5, 1, 3, 7])
        print("List +- custom", add_list_r, sub_list_r, '', sep='\n')
        return "end of main"
    return "just end"


main()
