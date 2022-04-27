class MyIterator:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index - 1]
        raise StopIteration


class MyList:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return MyIterator(self.lst)


l = MyList([1, 2, 3, 4, 5])
print(type(l))  # "l" is not a list, but MyList object

# but "l" contains elements and "l" is iterable
for i in l:
    print(i)