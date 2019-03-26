from lib.web.connection.browser import Browser
from lib.web.pages import (
    NewCommentPage,
    DuplicateCommentPage,
    MainPage,
    EditCommentPage,
)
from lib.web.elements import CommentsTable
from tests.tags import Tag


@Tag.from_name(tag_type='smoke')
def test_new_comment(browser: Browser) -> None:
    new_comment_page = NewCommentPage(browser)
    new_comment_page.open()
    new_comment_page.enter_comment_text("Test comment 30")
    new_comment_page.add_category(2)
    new_comment_page.save_and_return()
    comments_table = CommentsTable(browser)
    comments_table.load_another_table(4)
    assert comments_table.check_if_comment_is_present("Test comment 30")


@Tag.from_name(tag_type='smoke')
def test_duplicate(browser: Browser) -> None:
    duplicate_comment_page = DuplicateCommentPage(browser, 1)
    duplicate_comment_page.open()
    duplicate_comment_page.clear_number_field()
    duplicate_comment_page.save_and_return()
    comments_table = CommentsTable(browser)
    comments_table.load_another_table(4)
    assert comments_table.check_if_comment_is_present("Copy of Comment Text 1")


@Tag.from_name(tag_type='smoke')
def test_edit(browser: Browser) -> None:
    edit_comment_page = EditCommentPage(browser, 3)
    edit_comment_page.open()
    edit_comment_page.edit_comment("Edited comment")
    edit_comment_page.save_and_return()
    assert CommentsTable(browser).check_if_comment_is_present("Edited comment")


@Tag.from_name(tag_type='smoke')
def test_delete_one_comment(browser: Browser) -> None:
    main_page = MainPage(browser)
    main_page.open()
    main_page.delete(2)
    comments_table = CommentsTable(browser)
    assert not comments_table.check_if_comment_is_present("Comment Text 3")


@Tag.from_name(tag_type='smoke')
def test_delete_few_comments(browser: Browser) -> None:
    main_page = MainPage(browser)
    main_page.open()
    main_page.delete(2, 3)
    comments_table = CommentsTable(browser)
    assert not (
        comments_table.check_if_comment_is_present("Comment Text 3")
        and comments_table.check_if_comment_is_present("Comment Text 5")
    )


@Tag.from_name(tag_type='smoke')
def test_activate_one_comment(browser: Browser) -> None:
    main_page = MainPage(browser)
    main_page.open()
    main_page.select_action().activate(1)
    assert CommentsTable(browser).check_if_the_comment_is_active(1)


@Tag.from_name(tag_type='smoke')
def test_activate_few_comments(browser: Browser) -> None:
    main_page = MainPage(browser)
    main_page.open()
    main_page.select_action().activate(1, 3)
    comments_table = CommentsTable(browser)
    assert comments_table.check_if_the_comment_is_active(
        1
    ) and comments_table.check_if_the_comment_is_active(3)


@Tag.from_name(tag_type='smoke')
def test_inactivate_one_comment(browser: Browser) -> None:
    main_page = MainPage(browser)
    main_page.open()
    main_page.select_action().inactivate(1)
    assert CommentsTable(browser).check_if_comment_is_inactive(1)


@Tag.from_name(tag_type='smoke')
def test_inactivate_few_comments(browser: Browser) -> None:
    main_page = MainPage(browser)
    main_page.open()
    main_page.select_action().inactivate(1, 3)
    comments_table = CommentsTable(browser)
    assert comments_table.check_if_comment_is_inactive(
        1
    ) and comments_table.check_if_comment_is_inactive(3)
