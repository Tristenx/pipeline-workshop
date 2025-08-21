import pytest
from main import multiply


def test_multiply():
    assert multiply(2, 5) == 10
