import pytest


def add(x, y):
    return x + y


class TestAdd:

    @pytest.mark.smoke
    @pytest.mark.unit
    @pytest.mark.regression
    def test_positive(self):
        assert add(4, 6) == 10

    @pytest.mark.smoke
    @pytest.mark.unit
    @pytest.mark.regression
    def test_negative(self):
        assert add(-2, -3) == -5

    @pytest.mark.unit
    def test_zero(self):
        assert add(0, 0) == 0

    @pytest.mark.unit
    def test_big_num(self):
        assert add(99999999999, 99999999999) == 199999999998

    @pytest.mark.unit
    @pytest.mark.regression
    @pytest.mark.xfail(raises=TypeError, reason="illegal input")
    def test_illegal(self):
        assert add('a', 'b') == "ab"
