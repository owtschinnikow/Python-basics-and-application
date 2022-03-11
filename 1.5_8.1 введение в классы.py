"""
При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True
"""


class MoneyBox:
    def __init__(self, capacity):
        """
        # конструктор с аргументом – вместимость копилки
        """
        self.capacity = capacity
        self.number_of_coins = 0

    def can_add(self, v):
        """
        # True, если можно добавить v монет, False иначе
        :param v:
        :return:
        """



    def add(self, v):
        """
        # положить v монет в копилку
        :param v:
        :return:
        """
