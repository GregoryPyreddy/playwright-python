import sys
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description="Run pytest with specific test cases.")
    # Add a --tests argument that takes a list of test cases
    parser.add_argument("--tests", nargs='+', help="List of test cases to run")
    # Add an optional --test-file argument to specify the test file
    parser.add_argument("--test-file", help="Specify the test file", default="")
    # Add --run-browser and --namespace arguments
    parser.add_argument("--run-browser", help="Specify the browser to use", default="chromium")
    parser.add_argument("--namespace", help="Specify the namespace", default="dev02")
    # Parse the command-line arguments
    args = parser.parse_args()
    print(args.tests)
    tests = args.tests or ['test_TC10001', 'test2', 'test3']

    # Check if any tests were provided
    # if not args.tests:
    #     print("Usage: python run_tests.py --tests <test_case1> <test_case2> ...")
    #     sys.exit(1)

    # Create the test filter string
    test_filter = " or ".join(tests)
    command = ["pytest", "-s", "-k", test_filter]

    # Insert the test file into the command if provided
    if args.test_file:
        command.insert(1, args.test_file)

    # Add --browser and --name_space to the command
    if args.run_browser:
        command.extend(["--browser", args.run_browser])
    if args.namespace:
        command.extend(["--name_space", args.namespace])

    # Run the pytest command
    subprocess.run(command)

if __name__ == "__main__":
    main()