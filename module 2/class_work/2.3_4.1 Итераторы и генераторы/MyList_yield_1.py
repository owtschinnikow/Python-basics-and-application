class MyNoFilter2:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for x in self.lst:
            yield x


class MyNoFilter1:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.i < len(self.lst):
                self.i += 1
                return self.lst[self.i - 1]
            else:
                raise StopIteration

a = [i for i in range(5)]
print(list(MyNoFilter1(a))) # [0, 1, 2, 3, 4]
print(list(MyNoFilter2(a))) # [0, 1, 2, 3, 4]