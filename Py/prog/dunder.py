class Ele:
    def __init__(self, ele):
        self.item = ele

    def __add__(self, other):
        return self.item + other.item



e1 = Ele(10)
e2 = Ele(4)
print(e1+ e2)