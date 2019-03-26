from typing import Any
import pytest
from _pytest.mark import MarkDecorator
from tests.tags import TagError, Tag


@Tag.from_name(tag_type='unittest')
@pytest.mark.parametrize("tag_name", [
    (1,),
    ('azazaza',),
    (None,),
])
def test_tag_error(tag_name: Any) -> None:
    with pytest.raises(TagError):
        Tag.from_name(tag_name)


@Tag.from_name(tag_type='unittest')
def test_count_tags() -> None:
    assert len(Tag) == 2


@Tag.from_name(tag_type='unittest')
@pytest.mark.parametrize("tag_name, tag_type", [
    ('smoke', Tag.smoke),
    ('unittest', Tag.unittest),
])
def test_tag_from_name(tag_name: str, tag_type: Tag) -> None:
    assert Tag.from_name(tag_name) is tag_type.value


@Tag.from_name(tag_type='unittest')
def test_tag_name() -> None:
    assert Tag.smoke.name == 'smoke'


@Tag.from_name(tag_type='unittest')
def test_tag_value() -> None:
    assert isinstance(Tag.smoke.value, MarkDecorator)


@Tag.from_name(tag_type='unittest')
def test_tag_as_string() -> None:
    assert str(Tag.smoke) == 'smoke'
