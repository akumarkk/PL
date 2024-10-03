###### lambdas
- anonymous functions
- v => v*v lambda arg-list:expression
- sq = lambda v:v*v #sqaure of num; 
- caller sq(v)
- v => {}
- filter, map, reduce
- l = lambda v: 'yes' if v%2 ==0 else 'No'
- filter(lambda v:v%2==0, list) # where linq
- map(lambda v:v*2, sequence) # ret iter/ienumerable
- reduce(lambda v:v*2, sequence) from functools import reduce
- functools.reduce(lambda v, m:v+m, lst) #reduces to a value

###### decorators
 - param func, returns func with additional proc.
 - def decor(fun):
    def inner(p1, p2):
        res = fun()
        return res*2
    returm inner
- @decor
    def num():
        return 5
- caller num() or resFunc = decor(num)
- decor chaning

###### generators
 - yield 
 ```
 def gen(a, b):
    while a<b:
        yield a
    a = a+1
 ```
 - used instead of range like iter for customizing

 ###### modules
  - group of func, variables and classes
  - module name = py name
 - dir() - all mem of module/imported module
 - help(math) - doc of module
 - random module => from random import *; random(), randint(1, 50), uniform(1, 50)
 - rangerange(1, 12, 2)
 - choice(list) # choice random selection
 - 
###### list comprehensions
- one list from another list
- list = [expression for item in iterable if condition]
- z = [a[i] * b[i] for i in range(len(a))]
- 





