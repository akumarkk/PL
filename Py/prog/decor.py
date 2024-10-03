def decor(func):
    def inner(n):
        return func(n)/2
    return inner


def square(func):
    def inner(v):
        return v**2
    return inner

@square
@decor
def num(v):
    return v

print(num(100)) 



