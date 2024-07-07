class boo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


boo = boo()
print(boo.x)
del boo.x
print(boo.x)
boo.x = 10
print(boo.x)