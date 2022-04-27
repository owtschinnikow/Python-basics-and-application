class MyList:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def division(self, elem):
        return elem / 2

    def __next__(self):
        while True:
            if self.index < len(self.lst):
                self.index += 1
                return self.division(self.lst[self.index - 1])
            else:
                raise StopIteration


l = MyList([1, 2, 3, 4, 5])
print(type(l))  # "l" is not a list, but MyList object

# but "l" contains elements and "l" is iterable
for i in l:
    print(i)