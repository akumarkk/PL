import add
import pytest

def test_add():
    addObj = add.Add()
    assert addObj.sum(10, 25) == 25
    # assert(addObj.sum(10, 25), 25)

def test_add_30():
    addObj = add.Add()
    assert addObj.sum(10, 25) == 35
    # assert(addObj.sum(10, 25), 35)

# testadd()
