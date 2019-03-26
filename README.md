# Selenium web ui tests with python POM model
Contains web ui tests using POM most popular OOD pattern for Web UI automation using python programming language.

## Run automated tests
From the root directory of your shell run next command
- Smoke tests
```bash
➜ ./run-tests smoke
```
- Unittest tests
```bash
➜ ./run-tests unittest
```
- All tests
```bash
➜ ./run-tests all
```
### Auto-tests report
```bash
➜ ./run-tests all
============================================================================ test session starts ============================================================================
platform darwin -- Python 3.6.5, pytest-4.0.1, py-1.8.0, pluggy-0.9.0 -- /Users/vyah/.pyenv/versions/3.6.5/envs/python-tasks/bin/python
cachedir: .pytest_cache
rootdir: /Users/vyah/files/myprojects/comments-selenium-tests, inifile: pytest.ini
collected 15 items

tests/functional/tests_comments.py::test_new_comment PASSED                                                                                                           [  6%]
tests/functional/tests_comments.py::test_duplicate PASSED                                                                                                             [ 13%]
tests/functional/tests_comments.py::test_edit PASSED                                                                                                                  [ 20%]
tests/functional/tests_comments.py::test_delete_one_comment PASSED                                                                                                    [ 26%]
tests/functional/tests_comments.py::test_delete_few_comments PASSED                                                                                                   [ 33%]
tests/functional/tests_comments.py::test_activate_one_comment PASSED                                                                                                  [ 40%]
tests/functional/tests_comments.py::test_activate_few_comments PASSED                                                                                                 [ 46%]
tests/functional/tests_comments.py::test_inactivate_one_comment PASSED                                                                                                [ 53%]
tests/functional/tests_comments.py::test_inactivate_few_comments PASSED                                                                                               [ 60%]
tests/unit/test_tags.py::test_type_error[tag_name0] PASSED                                                                                                            [ 66%]
tests/unit/test_tags.py::test_type_error[tag_name1] PASSED                                                                                                            [ 73%]
tests/unit/test_tags.py::test_type_error[tag_name2] PASSED                                                                                                            [ 80%]
tests/unit/test_tags.py::test_count_types PASSED                                                                                                                      [ 86%]
tests/unit/test_tags.py::test_type_from_name[smoke-Tag.smoke] PASSED                                                                                                  [ 93%]
tests/unit/test_tags.py::test_type_from_name[unittest-Tag.unittest] PASSED                                                                                            [100%]

========================================================================= 15 passed in 8.65 seconds =========================================================================
removing .pytest_cache testing trash
environment is cleared
```

## Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all required python packages

