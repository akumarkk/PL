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

 ###### decorators





