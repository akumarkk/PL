
from functools import partial
def multiply(lst, v):
    return list(map(lambda i: i*v, lst))

def add(lst, v):
    
    return list(map(lambda i: i+v, lst))



l = [10, 20, 100]
multiply_by_2 = partial( multiply, v=2)
add_10 = partial( add, v=10)
lst = add_10( lst=multiply_by_2(lst=l))
print(lst)
