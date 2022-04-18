class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x) -> None:
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError


