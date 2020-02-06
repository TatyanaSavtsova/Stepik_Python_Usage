class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError("NonPositiveError")


a = PositiveList()
a.append(3)
a.append(-33)

print(a)