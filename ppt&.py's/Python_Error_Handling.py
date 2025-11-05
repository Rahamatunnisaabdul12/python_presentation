# Python Error Handling (try/except) with Logging
# --------------------------------------------------
# Demonstrating real-world error handling examples

import logging
import requests

# Configure logging
logging.basicConfig(filename="error_log.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# 1. Basic try/except example
try:
    x = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"ZeroDivisionError: {e}")
    print("Error: Cannot divide by zero!")

# 2. File Handling Example
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    logging.error(f"FileNotFoundError: {e}")
    print("File not found. Please check the filename.")

# 3. API Call Example
try:
    response = requests.get("https://api.github.com/user")
    response.raise_for_status()
    print("API call successful:", response.status_code)
except requests.exceptions.RequestException as e:
    logging.error(f"API Error: {e}")
    print("Error during API call.")

# 4. Using else and finally
try:
    num = int(input("Enter a number: "))
except ValueError as e:
    logging.error(f"ValueError: {e}")
    print("Invalid input! Please enter a number.")
else:
    print(f"You entered: {num}")
finally:
    print("Execution complete.")

# 5. Summary
"""
- try: block contains risky code
- except: handles specific exceptions
- else: executes if no exception occurs
- finally: runs always (for cleanup)
- logging: captures and stores errors for debugging
"""
