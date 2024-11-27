class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self._area = w * h

    @property
    def area(self):
        return self.w * self.h if self._area is None else self._area
    
    @area.setter
    def area(self, val):
        self._area = val



r = Rectangle(100, 10)
print(r.area)
r.area = 1010
print(r.area)