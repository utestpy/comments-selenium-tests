import pytest
from lib.web.urls import UrlError, WebUrl, Protocol, Http, Https, Ftp, Protocols
from tests.tags import Tag


_web_url_path: str = 'some/path/to/resource'


class FakeProtocol(Protocol):
    def as_str(self) -> str:
        return 'azazazaza'


@pytest.fixture(scope='module')
def protocols() -> Protocols:
    return Protocols()


@Tag.from_name(tag_type='unittest')
@pytest.mark.parametrize("protocol, as_str", [
    (Http(), 'http'),
    (Https(), 'https'),
    (Ftp(), 'ftp')
])
def test_protocol(protocol: Protocol, as_str: str) -> None:
    assert protocol.as_str() == as_str


@Tag.from_name(tag_type='unittest')
def test_number_of_protocols(protocols: Protocols) -> None:
    assert len(protocols) == 3


@Tag.from_name(tag_type='unittest')
def test_expected_set_of_protocols(protocols: Protocols) -> None:
    assert protocols.expected_set() == ('http', 'https', 'ftp')


@Tag.from_name(tag_type='unittest')
@pytest.mark.parametrize("protocol, as_str, url_path", [
    (Http(), 'http', 'http://some/path/to/resource'),
    (Https(), 'https', 'https://some/path/to/resource'),
    (Ftp(), 'ftp', 'ftp://some/path/to/resource')
])
def test_web_url(protocol: Protocol, as_str: str, url_path: str) -> None:
    assert WebUrl(protocol=protocol, path=_web_url_path).as_str() == url_path


def test_errored_web_url() -> None:
    with pytest.raises(UrlError):
        WebUrl(protocol=FakeProtocol(), path=_web_url_path).as_str()
