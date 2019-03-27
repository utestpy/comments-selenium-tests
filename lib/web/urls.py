from abc import ABC, abstractmethod
from typing import NamedTuple, Iterable


class Url(ABC):
    @abstractmethod
    def as_str(self) -> str:
        pass


class Protocol(ABC):
    @abstractmethod
    def as_str(self) -> str:
        pass


class UrlError(Exception):
    pass


class Http(Protocol):
    def as_str(self) -> str:
        return 'http'


class Https(Protocol):
    def as_str(self) -> str:
        return 'https'


class Ftp(Protocol):
    def as_str(self) -> str:
        return 'ftp'


class Protocols(NamedTuple):
    http: Protocol = Http()
    https: Protocol = Https()
    ftp: Protocol = Ftp()

    def expected_set(self) -> Iterable[str]:
        return tuple(self._asdict().keys())


class WebUrl(Url):
    def __init__(self, protocol: Protocol, path: str) -> None:
        self._protocols: Protocols = Protocols()
        self._protocol: Protocol = protocol
        self._path: str = path

    def _format_url(self):
        return f'{self._protocol.as_str()}://{self._path}'

    def as_str(self) -> str:
        web_url: str = self._format_url()
        expected_set: Iterable[str] = self._protocols.expected_set()
        if not web_url.startswith(expected_set):
            raise UrlError(f'WEB url should start with {expected_set}!')
        return web_url
