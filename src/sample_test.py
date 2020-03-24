import pytest


def test_passing():
    assert True


@pytest.mark.xfail
def test_failing():

    # This is a real comment.
    assert False
