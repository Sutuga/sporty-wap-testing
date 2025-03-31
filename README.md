# Test Task

---

### Requirements

1. Git
2. Python >= 3.8
3. Pipenv = *

> [!TIP]
> You can also see all requirements in the Pipfile.

### Installation Windows (Not tested on other OS systems)
* Create working directory for the project
* Clone repository to the working directory
* Install pipenv
  ```
  pip install --user pipenv
  ```

  > [!IMPORTANT]
  > Make sure that %USERPROFILE%\AppData\Roaming\Python\Python3X\Scripts\ in the path environment variable.
  > If not, add manually. Check pipenv correctly installed by ```pipenv -h```
    
* Go to the cloned repo in the working directory
* Install project dependencies
  ```
    pipenv sync --dev
  ```
  > [!TIP]
  > Or you can use ```pipenv install``` to re-lock your dependencies

### Run tests

```
pipenv run pytest tests -v
```

### Additional Information about the structure of the project

* **allure-report** - contains allure report
    * **index.html** - contains allure report in html format
*  **resources** - contains resources for the project
    * **general** - contains general resources related to the basic actions
    * **pages** - contains classes and methods related to the page object model
        * **common_page** - contains common methods for the page object model
    * **scenarios** - contains scenarios for the project
        * **common_scenarios** - contains common scenarios for the project
* **tests** - contains all tests
    * **allure-results** - contains allure results for current run
    * **screenshots** - contains screenshots for the current run
    * **test-search.py** - contains tests for the WAP
* **pipfile** - contains project dependencies
* **pyproject.toml** - contains project configuration
