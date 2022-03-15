"""
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д.

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
"""


class Buffer:
    def __init__(self):
        """
        Конструктор без аргументов.
        """
        self.list_buffer = []


    def add(self, *a):
        """
        Добавить следующую часть последовательности.
        :param a:
        :return:
        """
        self.list_buffer += a
        while len(self.list_buffer) // 5 > 0:
            print(sum(self.list_buffer[0:5]))
            self.list_buffer = self.list_buffer[5:]

    def get_current_part(self):
        """
        Вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены.
        """
        return self.list_buffer
