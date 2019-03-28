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
======================================================================================= test session starts =======================================================================================
platform darwin -- Python 3.6.5, pytest-4.0.1, py-1.8.0, pluggy-0.9.0 -- /Users/vyah/.pyenv/versions/3.6.5/envs/python-tasks/bin/python
cachedir: .pytest_cache
rootdir: /Users/vyah/files/myprojects/comments-selenium-tests, inifile: pytest.ini
collected 28 items

tests/functional/tests_comments.py::test_new_comment PASSED                                                                                                                                 [  3%]
tests/functional/tests_comments.py::test_duplicate PASSED                                                                                                                                   [  7%]
tests/functional/tests_comments.py::test_edit PASSED                                                                                                                                        [ 10%]
tests/functional/tests_comments.py::test_delete_one_comment PASSED                                                                                                                          [ 14%]
tests/functional/tests_comments.py::test_delete_few_comments PASSED                                                                                                                         [ 17%]
tests/functional/tests_comments.py::test_activate_one_comment PASSED                                                                                                                        [ 21%]
tests/functional/tests_comments.py::test_activate_few_comments PASSED                                                                                                                       [ 25%]
tests/functional/tests_comments.py::test_inactivate_one_comment PASSED                                                                                                                      [ 28%]
tests/functional/tests_comments.py::test_inactivate_few_comments PASSED                                                                                                                     [ 32%]
tests/unit/test_tags.py::test_tag_error[tag_name0] PASSED                                                                                                                                   [ 35%]
tests/unit/test_tags.py::test_tag_error[tag_name1] PASSED                                                                                                                                   [ 39%]
tests/unit/test_tags.py::test_tag_error[tag_name2] PASSED                                                                                                                                   [ 42%]
tests/unit/test_tags.py::test_count_tags PASSED                                                                                                                                             [ 46%]
tests/unit/test_tags.py::test_tag_from_name[smoke-smoke] PASSED                                                                                                                             [ 50%]
tests/unit/test_tags.py::test_tag_from_name[unittest-unittest] PASSED                                                                                                                       [ 53%]
tests/unit/test_tags.py::test_tag_name PASSED                                                                                                                                               [ 57%]
tests/unit/test_tags.py::test_tag_value PASSED                                                                                                                                              [ 60%]
tests/unit/test_tags.py::test_tag_as_string PASSED                                                                                                                                          [ 64%]
tests/unit/test_urls.py::test_protocol[protocol0-http] PASSED                                                                                                                               [ 67%]
tests/unit/test_urls.py::test_protocol[protocol1-https] PASSED                                                                                                                              [ 71%]
tests/unit/test_urls.py::test_protocol[protocol2-ftp] PASSED                                                                                                                                [ 75%]
tests/unit/test_urls.py::test_number_of_protocols PASSED                                                                                                                                    [ 78%]
tests/unit/test_urls.py::test_expected_set_of_protocols PASSED                                                                                                                              [ 82%]
tests/unit/test_urls.py::test_web_url[protocol0-http-http://some/path/to/resource] PASSED                                                                                                   [ 85%]
tests/unit/test_urls.py::test_web_url[protocol1-https-https://some/path/to/resource] PASSED                                                                                                 [ 89%]
tests/unit/test_urls.py::test_web_url[protocol2-ftp-ftp://some/path/to/resource] PASSED                                                                                                     [ 92%]
tests/unit/test_urls.py::test_azure_home_url PASSED                                                                                                                                         [ 96%]
tests/unit/test_urls.py::test_errored_web_url PASSED                                                                                                                                        [100%]

==================================================================================== 28 passed in 9.47 seconds ====================================================================================
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

