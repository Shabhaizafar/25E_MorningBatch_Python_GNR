class MyContext:
    def __enter__(self):
        print("Entering...")
        return "Resource Ready"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")
        if exc_type:
            print(f"Error: {exc_val}")
        return True  # suppresses the exception

with MyContext() as val:
    print(val)
    # raise ValueError("Oops!")  # Try uncommenting this to test exception handling
