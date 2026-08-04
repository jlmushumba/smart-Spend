# Helper function for reading a file

def read_file(path: str):

    if not isinstance(path, str):
        return "The path not found!"

    try:

        with open(path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError as e:
        print(f"Error: {e}")

    except Exception as error:
        print(f"{error}")
    