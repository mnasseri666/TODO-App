class Sorter:
    def __init__(self, tasks):
        self.tasks = tasks

    def alphabet(self):
        return sorted(self.tasks, key=lambda task: task[2].casefold())

    def time(self):
        return sorted(self.tasks, key=lambda task: task[1])


if __name__ == "__main__":
    x = Sorter("mahana")
    print(x.alphabet())
