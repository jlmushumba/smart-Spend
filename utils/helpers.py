# Helper function for reading a file
import json
from datetime import datetime

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


def recent_id(file_path):
    """
    Return recent ID in json file
    """
    try:

        with open (file_path, "r") as file:
            budgets = json.load(file)
            if budgets:
                    return budgets[-1]['id'] + 1
            #else:
                    #recent_id = 0
            #recent_id = expenses[-1]['id']
    except FileNotFoundError as error:
        pass
        #print(f"Error: {error}")
    except json.JSONDecodeError:
        pass
        #recent_id = 0

    return 0
