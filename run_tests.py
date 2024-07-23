import sys
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description="Run pytest with specific test cases.")
    # Add a --tests argument that takes a list of test cases
    parser.add_argument("--tests", nargs='+', help="List of test cases to run")
    # Add an optional --test-file argument to specify the test file
    parser.add_argument("--test-file", help="Specify the test file", default="")
    # Add --browser and --namespace arguments
    parser.add_argument("--browser", help="Specify the browser to use", default="")
    parser.add_argument("--name_space", help="Specify the namespace", default="")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if any tests were provided
    if not args.tests:
        print("Usage: python run_tests.py --tests <test_case1> <test_case2> ...")
        sys.exit(1)

    # Create the test filter string
    test_filter = " or ".join(args.tests)
    command = ["pytest", "-k", test_filter]

    # Insert the test file into the command if provided
    if args.test_file:
        command.insert(1, args.test_file)

    # Add --browser and --namespace to the command
    if args.browser:
        command.extend(["--browser", args.browser])
    if args.namespace:
        command.extend(["--name_space", args.namespace])

    # Run the pytest command
    subprocess.run(command)

if __name__ == "__main__":
    main()