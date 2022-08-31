import pytest

@pytest.fixture()
def text_first():
    print('hello')


def test_second(text_first):
    assert 1 == 1