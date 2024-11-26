from typing import TypeVar
V = TypeVar('V')

def testfunc(v: V):
    print(v)

testfunc('hello')
testfunc(100)