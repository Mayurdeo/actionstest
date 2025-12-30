from src.functions import add,sub
    

def test_add():
    assert add(2,3)==5
    assert add(-1,2)==1

def test_sub():
    assert sub(2,3)==-1
    assert sub(-1,2)==-3