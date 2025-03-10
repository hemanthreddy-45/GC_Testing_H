import argparse  # Import argparse to handle arguments

def generate_test(suite_type):
    print(f"Running test suite: {suite_type}")  # Print the test suite type

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Chatbot Test Generator")
    parser.add_argument('--suite_type', type=str, required=True, help='Type of test suite (e.g., smoke, regression, etc.)')

    try:
        # Parse the arguments
        args = parser.parse_args()  # This will process the arguments

        print(f"Parsed suite_type argument: {args.suite_type}")  # Debug print to check parsed argument

        # Call the function with the parsed argument
        generate_test(args.suite_type)  # We pass the value of --suite_type directly
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Ensure you are passing the argument correctly. Example: python3 chatbot_test_generator.py --suite_type='smoke'")
