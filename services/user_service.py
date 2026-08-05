import json
from models.user import User

def create_profile(user_name, user_email, user_currency):

    """
    Creates new profile and saves it in assets/profile.json
    """

    user = User(user_name, user_email, user_currency)
    data = user.to_dict()
    with open ("data/profile.json", "w") as file:
        json.dump(data, file, indent=4)

def view_profile():
    """
    It views the content of models/profile.json (profile)
    """
    with open ("data/profile.json", "r") as file:
        contents = json.load(file)
    return contents

def edit_profile(name = None, email = None, currency= None):
    """
    It changes the user's pre-existing data accordingly
    """
    if not edit_profile:
        return None