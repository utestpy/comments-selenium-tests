from selenium.webdriver import Remote


class Browser:
    def __init__(self, url: str) -> None:
        self._client: Remote = Remote(command_executor=url)

    def __getattr__(self, attribute_name: str) -> None:
        return getattr(self._client, attribute_name)
