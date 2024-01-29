- Name - sanddeep
- Author - sanddep


### Web Automation Framework with POM in Python(Selenium)

- Python, PyTest
- Selenium
- Allure Report
- Gitignore, PyTest Report
- Page Object Model and Page Factory both
- Highlight element while run
- Parallel Run with xdist
- MY SQL data base connect to verify data.

## Folder Structure

<img width="944" alt="Screenshot 2023-08-28 at 5 28 26 PM" src="https://github.com/PramodDutta/PyWebAutomation0x/assets/1409610/629dd569-5a7f-4293-a821-7af6f97786cc">



# CI/CD Run


<img width="1199" alt="Screenshot 2023-08-28 at 5 28 46 PM" src="https://github.com/PramodDutta/PyWebAutomation0x/assets/1409610/b339baf7-ae46-4188-b285-bfb88862f752">





- pip install pytest-dotenv
- pip install selenium
- pip install allure-pytest requests
- pip install pytest selenium pytest-html openpyxl 
- pip install selenium-page-factory 
- pip install pyyaml faker openpyxl
- pip install pytest-xdist 
- pip install mysql-connector-python
- pip install pytest-reportportal

## Running parallelly
- pytest -n auto tests/vwoLoginTests/pom/test_*

## specific testcase to run
- pytest -n auto -k "smoke" tests/vwoLoginTests/pom/test_*

- pytest -n auto "tests/vwoLoginTests/test_vwologin.py" -s -v --alluredir = allure-results
- allure serve allure-results
- pytest -n auto "tests/vwoLoginTests/test_vwologin.py" -s -v 
- allure generate


## bdd to run 
- behave -f allure_behave.formatter:AllureFormatter -o allure-reports ./features
- allure serve allure-reports
