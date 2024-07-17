import importlib.util


def execute_tutorial(tutorial_number):
    tutorial_module = f"tutorial_{tutorial_number}.main"
    try:
        module = importlib.import_module(tutorial_module)
    except ModuleNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # tutorial_number = int(input("Enter tutorial number (e.g., 1, 2, 3): "))
    tutorial_number = 1
    execute_tutorial(tutorial_number)
