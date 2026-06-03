"""测试 add.py — DevOpsAgent GitLab 工作流验证用。"""

import pytest
from add import add, subtract, multiply, divide


class TestAdd:
    def test_positive(self):
        assert add(2, 3) == 5

    def test_negative(self):
        assert add(-1, -1) == -2

    def test_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5


class TestSubtract:
    def test_basic(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(3, 5) == -2


class TestMultiply:
    def test_basic(self):
        assert multiply(3, 4) == 12

    def test_zero(self):
        assert multiply(0, 100) == 0


class TestDivide:
    def test_basic(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(5, 2) == 2.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="除数不能为零"):
            divide(1, 0)
