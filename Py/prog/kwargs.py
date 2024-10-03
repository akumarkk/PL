def func1(a, *args, **kwargs):
    print("args {0} *args = {1} kwargs = {2}".format(a, args, kwargs))

func1("avar", 10, 20, 0, name='stud', age=10)