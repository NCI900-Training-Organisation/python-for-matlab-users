try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle a specific error
    print("Cannot divide by zero!")
except Exception as e:
    # Code to handle any other exception
    print(f"An error occurred: {e}")
else:
    # Code that runs if no exception was raised
    print("Division successful:", result)
finally:
    # Code that always runs, regardless of whether an exception occurred
    print("Execution completed.")

'''
* try: Contains code that might raise an exception.
* except: Catches specific or general exceptions and handles them.
* else: Executes if no exceptions are raised in the try block.
* finally: Runs no matter what, useful for cleanup tasks (e.g., closing files or releasing resources)
'''