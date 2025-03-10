import sys

def generate_test(suite_type):
    # Using old-style string formatting (works in Python 2 and 3)
    print("Running test suite: %s" % suite_type)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Missing arguments. Usage: python3 chatbot_test_generator.py --suite_type=<type>")
        sys.exit(1)
    
    # Get the argument value directly
    suite_type = sys.argv[1]
    generate_test(suite_type)
