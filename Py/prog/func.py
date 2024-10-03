def func1(lst):
    print("func1")
    print(lst, type(lst))

def func(f, args):
    print("func")
    f(args)

func(func1, "hello")
func(func1,[10, 20])
func(func1,{'k': 'v'})