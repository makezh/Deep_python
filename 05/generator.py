from pathlib import Path


def file_gen(file_name: str,
             words: list[str] = None,
             path: str = str(Path().cwd())):
    if words is None:
        words = []

    with open(path + '/' + file_name, 'r', encoding='utf-8') as file:
        for row in file:
            row_list = row.lower().split()
            in_file = False
            for word in words:
                if word in row_list:
                    in_file = True
                    break
            if in_file:
                row = row.rstrip()
                yield row

    return "over"


def main():
    if __name__ == '__main__':
        file_name = 'test_txt.txt'
        words = ['текст']
        for row in file_gen(file_name, words):
            print(row)
        return "end of main"
    return "just end"


main()
