from tox_example import main


def test_count():
    a = 3
    b = 1
    res = main.add(a, b)
    assert res == 4
