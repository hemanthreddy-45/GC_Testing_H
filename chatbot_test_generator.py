import argparse

def generate_test(suite_type):
    print(f"Running test suite: {suite_type}")

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Chatbot Test Generator")
    parser.add_argument('--suite_type', type=str, required=True, help='Type of test suite (e.g., smoke, regression, etc.)')

    # Parse the arguments
    args = parser.parse_args()

    # Call the function with the parsed argument
    generate_test(args.suite_type)
