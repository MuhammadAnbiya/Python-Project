from hello import hello

def test_default():
    assert hello() == "Hello, World"

def test_argument():
    for name in ["Harmonie", "Harry", "Roy"]:
        assert hello(name) == f"Hello, {name}"


