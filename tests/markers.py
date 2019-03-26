import pytest
from _pytest.mark import MarkDecorator


class TestType:
    smoke: MarkDecorator = pytest.mark.smoke
