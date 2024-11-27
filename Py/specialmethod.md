##### Special methods

__repr__
- used by repr, Unambiguous, machine-readable
- When you use repr() on an object or when you need a string that can be evaluated to recreate the object.

__str__
- used by str, Prioritize readability and conciseness


In Python, the __call__ method is a special method that allows instances of a class to be called like functions. This means you can use parentheses () to invoke the object, triggering the execution of the __call__ method.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return self.factor * number

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # Output: 10
print(triple(10))  # Output: 30

