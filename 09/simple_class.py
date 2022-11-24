import cProfile
import io
import pstats
import time

N = 500_000


class Department:
    def __init__(self, employee):
        self.employee = employee


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.department = Department(self)
        self.company = [[Department(self)] * 10]


def main():
    if __name__ == "__main__":
        print(f"N = {N}\n")

        pr = cProfile.Profile()
        pr.enable()

        print("[Simple] Создание пачки экземпляров")
        start_1 = time.time()

        workers = [Employee("Name", 35) for _ in range(N)]

        end_1 = time.time()
        print(f"Время работы: {end_1 - start_1} сек.\n")

        print("[Simple] доступ/изменениe/удалениe атрибутов")
        start_2 = time.time()

        for _ in range(N):
            worker = Employee("Name", 30)
            worker.name = "New_name"
            worker.department = Department(worker)
            del worker

        end_2 = time.time()
        print(f"Время работы: {end_2 - start_2} сек.\n")

        pr.disable()

        s = io.StringIO()
        sort_by = "cumulative"
        ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)
        ps.print_stats()
        print(s.getvalue())


main()
