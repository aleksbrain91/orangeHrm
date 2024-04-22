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

# Running Tests with `runner.py`

## Basic Usage

**Run tests in normal mode:**
```bash
python runner.py testNormal
```

**Run tests in headless mode:**
```bash
python runner.py testHeadless
```

## Parallel Execution

**Run tests in parallel:**
```bash
python runner.py testNormal --parallel
python runner.py testHeadless --parallel
```

**Run tests in parallel, filtering by specific groups:**
```bash
python runner.py testNormal --parallel --group=group1
python runner.py testHeadless --parallel --group=group1
```

## Running Specific Tests

**Run a specific test file in normal mode:**
```bash
python runner.py testNormal --test=test/test_case_1_Login_to_the_application.py
```

**Run a specific test file in headless mode:**
```bash
python runner.py testHeadless --test=test/test_case_1_Login_to_the_application.py
```

## Additional Information

- The `--parallel` flag enables parallel execution across multiple instances. If combined with the `--group` flag, only tests marked with the specified group will be executed. Without the `--group` flag, all applicable tests will be executed in parallel.
- The `--test` flag allows for running a specific test. When this flag is used, the specified test file is executed independently of other tests, regardless of the group marking within the file.
- When tests from one file are executed in parallel, they will share the same browser instance. If you need to run multiple tests from the same file in separate browser instances, you may need to split the tests across different files or manually control their execution.
```
