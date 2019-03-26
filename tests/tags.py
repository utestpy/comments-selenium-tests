from enum import Enum
import pytest
from _pytest.mark import MarkDecorator


class TagError(Exception):
    pass


class Tag(Enum):
    smoke: 'Tag' = pytest.mark.smoke
    unittest: 'Tag' = pytest.mark.unittest

    @classmethod
    def from_name(cls, tag_type: str) -> MarkDecorator:
        for next_tag in cls:
            if next_tag.name == tag_type:
                return next_tag.value
        raise TagError(f'{tag_type} is unknown!')
