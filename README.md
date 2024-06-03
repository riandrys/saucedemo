# Selenium Automated Testing with Allure Reporting

This repository contains a Selenium-based test automation framework using Python, Pytest, and Page Object Model (POM) with Allure for reporting.

## Requirements

- Python 3.7+
- Google Chrome, Firefox or Safari browser
- Allure Commandline

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/riandrys/saucedemo.git
    cd saucedemo
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Install Allure Commandline:**

    Make sure Java version 8 or above installed, and its directory is specified in the JAVA_HOME environment variable.

    **On macOS:**

    ```sh
    brew install allure
    ```

    **On Linux:**

    ```sh
    sudo apt-add-repository ppa:qameta/allure
    sudo apt-get update
    sudo apt-get install allure
    ```

    **On Windows:**

    - Go to [official website](https://allurereport.org/docs/install-for-windows/) and follow the instructions.

    **Verify the installation:**

    ```sh
    allure --version
    ```

## Configuration

Ensure you have a `.env` file in the root of your project with the following content:

```env
BASE_URL=https://www.example.com
AFTER_LOGIN_URL = https://www.example.com
USERNAME=your_username
PASSWORD=your_password
```

You can copy the `.env.example`
```shell
cp .env.example .env
```

## Running the Tests
```shell
pytest # Run all tests in Chrome by default
pytest --browser firefox # Run tests in Firefox
pytest --browser safari # Run tests in Safari, run safaridriver --enable in terminal first
pytest --headless # Run tests in headless mode
```

## Generating Allure Report

```shell
allure serve reports/allure-results
```
