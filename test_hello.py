from hello import add

def test_add():
    assert 2 == add(1,1)

#list: code: pylint --disable=R,C hello.py
# test: python -m pytest -vv --cov=hello test_hello.py