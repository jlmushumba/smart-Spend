import json
from models.user import User

def create_profile(user_name = None, user_email = None, user_currency = None):

    """
    Creates new profile and saves it in assets/profile.json
    """
   
    try:

        user = User(user_name, user_email, user_currency)
        data = user.to_dict()
        with open ("data/profile.json", "w") as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError as error:
        print(f"Error: {error}")

def view_profile():
    """
    It views the content of data/profile.json (profile)
    """
    if not "data/profile.json":
        raise ValueError('No profile found!')
    try:

        with open ("data/profile.json", "r")  as file:
            contents = json.load(file)
            return contents
    except FileNotFoundError as e1:
        print(f"Error: {e1}")
    

def edit_profile(data: dict):
    """
    It changes the user's pre-existing data accordingly
    """

    try:

        with open ("data/profile.json", "r+") as file :
            contents = json.load(file)

            for key, value in data.items():
                contents[key] = value
            file.seek(0)
            json.dump(contents, file, indent=4)
            file.truncate()

        

    except FileNotFoundError as error:
        print(f"Error: {error}")