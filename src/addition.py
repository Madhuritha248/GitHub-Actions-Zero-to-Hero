# app.py
# This is a test commit
#this is addition method adding a and b 
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
