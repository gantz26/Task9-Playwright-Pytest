# Summary

This repository contains auto tests for verifying login, cart operations, checkout, contact form and place order on the [Automation Exercise](https://www.automationexercise.com/) website.

## Requirements

The next requirements must be completed to run tests:
1. Install [PyCharm](https://www.jetbrains.com/pycharm/)
2. Install [Python](https://www.python.org/)

## Steps to install, launch and creating a report

1. Make a copy of this repository:
```
git clone https://github.com/gantz26/Task9-Playwright-Pytest.git
```

2. Open this folder in PyCharm and install all dependencies and create data folder:
```
mkdir data
pip install pipenv
pipenv install
playwright install
```

3. To run the tests use one of the next commands:
```
pytest
```

4. To generate and view a report:
```
allure serve allure-results
```