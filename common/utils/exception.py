import traceback


def handle_exception(e: Exception):
    print_exception(e)


def print_exception(e: Exception):
    print(f"ERROR: {str(e)}")
    traceback.print_exc()
