from typing import Protocol
class Numeric(Protocol):
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value


class AnotherNumeric(Numeric):
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value

class AnotherNumericProto(Numeric):
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value

class AnotherNumeric1:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value

def add(a: AnotherNumeric, b:AnotherNumeric):
    return a+b

n1 = AnotherNumericProto(10)
n2 = AnotherNumericProto(20)

print(add(n1, n2))

    
