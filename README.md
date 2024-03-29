# Project Setup and Testing Guide

This guide covers the setup process for running automated tests in the project, generating reports with Allure, and configuring PyCharm for test execution.

## Prerequisites

- Python 3.x
- PyCharm or any other IDE/Text Editor

## Installation

### Install Required Packages

Install all required packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Install Allure Command Line

- **macOS**: Install Allure using Homebrew with the following command:

```bash
brew install allure
```

- **Windows**:

1. Download the latest Allure Commandline zip from the [Allure Releases Page](https://github.com/allure-framework/allure2/releases).
2. Unzip the contents to a directory (e.g., `C:\Allure`).
3. Add the `bin` directory from the unzipped location to your system's PATH environment variable. Detailed instructions can be found [here](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).

For more detailed Allure installation instructions, visit the [Allure Documentation](https://docs.qameta.io/allure/).

## PyCharm Run Configurations

Set up run configurations in PyCharm to easily run tests and open reports:

1. Open PyCharm and navigate to `Run` > `Edit Configurations`.
2. Click the `+` button to add a new Python configuration.
3. Name the configuration (e.g., "Run All Tests").
4. Script path: Choose the path to your `runner.py` script.
5. Parameters: Enter the specific command (e.g., `test`, `testHeadless`, or `openReport`).
6. Repeat steps 2-5 to create configurations for `testHeadless` and `openReport`.

## Running Tests from the Console

Besides using PyCharm configurations, you can run tests directly from the console:

### Run All Tests

```bash
python runner.py testNormal
```

### Run All Tests in Headless Mode

```bash
python runner.py testHeadless
```

### Open Allure Report

```bash
python runner.py openReport
```

### Run Specific test by name

```bash
python runner.py --test=test/test_case_1_Login_to_the_application.py --headless
```
```bash
python runner.py --test=test/test_case_1_Login_to_the_application.py
```