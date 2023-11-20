import os
import subprocess
from pathlib import Path

test_folder = "test"

test_files = []
all_files = os.listdir(test_folder)
for filename in all_files:
   if filename.endswith(".in"):
        test_files.append(filename)


def execute_test(input_file, script, execution_type, script_flags):
    input_path = os.path.join(test_folder, input_file)
    if script=='date.py':
        with open(input_path, "r") as expected_output:
            input_path = expected_output.read()
    expected_output_path = os.path.join(test_folder, input_file.replace(".in", f"{script_flags.split(' ')[0]}.out"))
    if execution_type == 'stdin':
        expected_output_path = expected_output_path.replace('.out', '.stdin.out')

    try:
        print(f"Test Input: {input_path}")
        if execution_type == "stdin" and script !='date.py':
            command = f"python {script} {script_flags} < {input_path}"
        else:
            command = f"python {script} {Path(input_path).as_posix()} {script_flags}"
        print(command)
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        print("Execution Command:", result.args)
        print("output",result.stdout)

        if result.stdout:
            print("Expected Output Path:", expected_output_path)
            try:
                with open(expected_output_path, "r") as expected_output:
                    expected_result = expected_output.read()
                    if result.stdout == expected_result:
                        return "PASS", None, result.returncode, expected_result
                    else:
                        return "FAIL", f"Output Mismatch!\nGot:\n{result.stdout}", 1, expected_result
            except FileNotFoundError:
                return "FAIL", f"File Not Found!\n{expected_output_path}", 1, ''

    except Exception as e:
        return "ERROR", str(e)

def main():
    test_results = {"Passed": 0, "Failed": 0, "WordCount_Tests": 0, "gron_test": 0, "Date_Tests": 0}
    total_tests = 0
    test_flags = {
        "wordcount": ['', '-l', '-w', '-c'],
        "gron": ['','-o obj'],
        "date": ['']
    }

    for test_file in test_files:
        if test_file.startswith('wc'):
            script_name = "wc.py"
            test_results["WordCount_Tests"] += 1
            additional_flags = test_flags['wordcount']
        elif test_file.startswith('gron'):
            script_name = "gron.py"
            test_results["gron_test"] += 1
            additional_flags = test_flags['gron']
        elif test_file.startswith('date'):
            script_name = "date.py"
            test_results["Date_Tests"] += 1
            additional_flags = test_flags['date']

        for execution_type in ["cli", "stdin"]:
            for flag in additional_flags:
                status, error_message, exit_code, expected_result = execute_test(test_file, script_name, execution_type, flag)
                total_tests += 1
                if exit_code > 0:
                    test_results['Failed'] += 1
                else:
                    test_results['Passed'] += 1

                print(f"{status} \n\tTest Case: {test_file.split('.')[0]} {test_file.split('.')[1]}\n")
                print(f"\tExecution Type: {execution_type.upper()}")
                print(f"\tExit Code: {exit_code}")

                if error_message:
                    print(f"Error Message:\n{error_message}\n")
                    print(f"Expected Result:\n{expected_result}\n")
                print("-----------------------------------------------------------------")

        print("-----------------------------------------------------------------")

    for result, count in test_results.items():
        print(f"{result} : {count}")
    print(f"TOTAL  : {total_tests}")

    if test_results['Failed'] > 0:
        print("Some tests failed.")
        exit_code = 1
    else:
        print("All tests passed.")
        exit_code = 0

    exit(exit_code)

if __name__ == "__main__":
    main()