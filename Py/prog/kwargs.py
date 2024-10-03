def func1(a, *args, **kwargs):
    print("args {0} *args = {1} kwargs = {2}".format(a, args, kwargs))

def func2(a, *args, **kwargs):
    func1(args, kwargs)
    func1(*args, **kwargs)


func1("avar",  name='stud', age=10)
func2("avar",  name='stud', age=10)