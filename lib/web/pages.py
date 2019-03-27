from abc import ABC, abstractmethod
from lib.web.connection.browser import Browser
from lib.web.elements import (
    CommentsTable,
    SelectActionDropDown,
    save_and_return,
    find_text_field,
    enter_comment_text,
)
from lib.web.urls import Url, WebUrl, Protocols


def _move_to_comment_editing(browser: Browser, comment_to_select: int, value: str):
    MainPage(browser).open()
    CommentsTable(browser).select_comment(comment_to_select)
    browser.find_element_by_css_selector(f'input[value="{value}"]').click()


class BasePage(ABC):
    @abstractmethod
    def open(self) -> None:
        pass


class MainPage(BasePage):
    def __init__(self, browser: Browser) -> None:
        self._browser = browser
        self._url: Url = WebUrl(protocol=Protocols().http, path="commentssprintone.azurewebsites.net")

    def open(self) -> None:
        self._browser.get(self._url.as_str())

    def delete(self, *comment_numbers: int) -> None:
        for comment in comment_numbers:
            CommentsTable(self._browser).select_comment(comment)
        self._browser.find_element_by_css_selector('input[value="Delete"').click()
        self._browser.find_element_by_css_selector("span.ui-button-text").click()

    def select_action(self) -> SelectActionDropDown:
        return SelectActionDropDown(self._browser)


class NewCommentPage(BasePage):
    def __init__(self, browser: Browser) -> None:
        self._browser = browser

    def open(self) -> None:
        MainPage(self._browser).open()
        self._browser.find_element_by_id("newbutton").click()

    def enter_comment_text(self, comment_text: str) -> None:
        enter_comment_text(self._browser, comment_text)

    def add_category(self, category_number: int) -> None:
        self._browser.find_element_by_xpath(
            f"//div[@class='categoryitem'][{category_number}]"
            f"/input[@id='Categories']"
        ).click()
        self._browser.find_element_by_css_selector('input[onclick="SelectCur()"]').click()

    def save_and_return(self) -> None:
        save_and_return(self._browser)


class DuplicateCommentPage(BasePage):
    def __init__(self, browser: Browser, comment_to_duplicate: int) -> None:
        self._browser = browser
        self.comment_to_duplicate = comment_to_duplicate

    def open(self) -> None:
        _move_to_comment_editing(
            self._browser, self.comment_to_duplicate, value="Duplicate..."
        )

    def clear_number_field(self) -> None:
        self._browser.find_element_by_id("Number").clear()

    def save_and_return(self) -> None:
        save_and_return(self._browser)


class EditCommentPage(BasePage):
    def __init__(self, browser: Browser, comment_to_edit: int) -> None:
        self._browser = browser
        self.comment_to_edit = comment_to_edit

    def open(self) -> None:
        _move_to_comment_editing(self._browser, self.comment_to_edit, value="Edit..")

    def edit_comment(self, edited_comment_text: str) -> None:
        find_text_field(self._browser).clear()
        enter_comment_text(self._browser, edited_comment_text)

    def save_and_return(self) -> None:
        save_and_return(self._browser)
