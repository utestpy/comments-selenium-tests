from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from lib.web.connection.browser import Browser


def save_and_return(browser: Browser) -> None:
    browser.find_element_by_css_selector('input[value="Save & Return"]').click()


def find_text_field(browser: Browser) -> WebElement:
    return browser.find_element_by_id("Text")


def enter_comment_text(browser: Browser, comment_text: str) -> None:
    find_text_field(browser).send_keys(comment_text)


class CommentsTable:
    def __init__(self, browser: Browser) -> None:
        self._browser = browser

    def load_another_table(self, table_number) -> None:
        self._browser.get(f"http://commentssprintone.azurewebsites.net/?page={table_number}")

    def check_if_comment_is_present(self, comment_text: str) -> bool:
        try:
            return self._browser.find_element_by_xpath(f'//td[text()="{comment_text}"]').is_displayed()
        except NoSuchElementException:
            return False

    def select_comment(self, comment_number: int) -> None:
        self._browser.find_element_by_xpath(
            f"//tbody/tr[@class='webgrid-alternating-row']"
            f"[{comment_number}]/td[@class='checkedcolumn']"
        ).click()

    def select_active_comment(self, comment_number: int) -> None:
        self._browser.find_element_by_xpath(
            f"//tbody/tr[@class='webgrid-row-style']"
            f"[{comment_number}]/td[@class='checkedcolumn']"
        ).click()

    def check_if_the_comment_is_active(self, comment_number: int) -> bool:
        if (
            self._browser.find_element_by_xpath(
                f"//tr[@class='webgrid-alternating-row'][{comment_number}]"
                f"/td[@class='inactivecolumn']"
            ).text
            == ""
        ):
            return True
        return False

    def check_if_comment_is_inactive(self, comment_number: int) -> bool:
        if (
            self._browser.find_element_by_xpath(
                f"//tr[@class='webgrid-row-style'][{comment_number}]"
                f"/td[@class='inactivecolumn']"
            ).text
            == "V"
        ):
            return True
        return False


class SelectActionDropDown:
    def __init__(self, browser: Browser) -> None:
        self._browser = browser

    def activate(self, *comment_numbers: int) -> None:
        for comment in comment_numbers:
            CommentsTable(self._browser).select_comment(comment)
        self._click_actions_drop_down()
        self._browser.find_element_by_css_selector('option[value="Activate"]').click()

    def inactivate(self, *comment_numbers: int) -> None:
        for comment in comment_numbers:
            CommentsTable(self._browser).select_active_comment(comment)
        self._click_actions_drop_down()
        self._browser.find_element_by_css_selector('option[value="Inactivate"]').click()

    def _click_actions_drop_down(self) -> None:
        self._browser.find_element_by_id("commandSelect").click()
