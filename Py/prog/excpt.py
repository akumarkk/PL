

class OverTheLimitException(Exception):
    def __init__(self, msg):
        self.msg = msg

def limitexcepvalidate():
    print("validating ...")
    raise OverTheLimitException("you can't withdraw more then 500$")


try:
    limitexcepvalidate()
except OverTheLimitException as obj:
    print("over the limit except {}".format(obj))

a, b = [int(v) for v in input().split()]
try:
    print(a/b)
except Exception:
    print("exception")
else:
    print("no exception...")

finally:
    print("resource rel...")
    # close file




print("end...")