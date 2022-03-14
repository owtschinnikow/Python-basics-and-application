"""
При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True
"""


class MoneyBox:
    def __init__(self, capacity):
        """
        Конструктор с аргументом – вместимость копилки.
        """
        self.capacity = capacity
        self.number_of_coins = 0

    def can_add(self, v):
        """
        True, если можно добавить v монет, False иначе.
        :param v:
        :return:
        """
        if self.capacity - self.number_of_coins - v >= 0:
            return True
        return False

    def add(self, v):
        """
        Положить v монет в копилку.
        :param v:
        :return:
        """
        if self.can_add(v):
            self.number_of_coins += v
