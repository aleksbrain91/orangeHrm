import subprocess
import sys
import os
import shutil

# Windows example: r'C:\Users\YOUR_USERNAME\allure-2.27.0\allure-2.27.0\bin\allure.bat'
ALLURE_COMMAND_PATH = r'C:\allure-2.27.0\bin\allure.bat'

def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def open_allure_report():
    report_dir = "allure-report"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    subprocess.call([ALLURE_COMMAND_PATH, 'serve', 'allure-results'])

def generate_allure_report():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    results_dir = os.path.join(base_dir, "allure-results")
    report_dir = os.path.join(base_dir, "allure-report")
    subprocess.call([ALLURE_COMMAND_PATH, 'generate', results_dir, '-o', report_dir, '--clean'])

def run_tests_and_generate_report(test_name=None, headless=False):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    results_dir = os.path.join(base_dir, "allure-results")
    clear_directory(results_dir)
    clear_directory(os.path.join(base_dir, "allure-report"))

    pytest_cmd = ['pytest']
    if test_name:
        pytest_cmd.append(test_name)
    pytest_cmd.append(f'--alluredir={results_dir}')
    if headless:
        pytest_cmd.append('--headless')

    subprocess.call(pytest_cmd)
    generate_allure_report()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'openReport':
            open_allure_report()
        elif command == 'testHeadless':
            run_tests_and_generate_report(headless=True)
        elif command == 'testNormal':
            run_tests_and_generate_report(headless=False)
        elif command.startswith('--'):
            # Additional parsing for --test and --headless flags
            test_name = None
            headless = False
            for arg in sys.argv[1:]:  # Skip the script name
                if arg.startswith('--test='):
                    test_name = arg.split('=')[1]
                elif arg == '--headless':
                    headless = True
            run_tests_and_generate_report(test_name=test_name, headless=headless)
        else:
            print(f"Unknown command: {command}")
    else:
        print("No command provided.")