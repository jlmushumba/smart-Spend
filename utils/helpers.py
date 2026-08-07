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


def edit_profile_data():
    data_to_edit = print(
                    "What do you want to change ? (Enter the corresponding number) \n 1. name\n 2. email 3. currency"
                    )
    edit_choice = input(">> ")

    if edit_choice == "1":
        new_name = input("Enter new name: ")
        return {"name" : new_name}
        

    elif edit_choice == "2":
        new_email = input("Enter your new email: ")
        return {"email" : new_email}

    elif edit_choice == "3":
        new_currency = input("Enter new currency: ")
        return {"currency" : new_currency}

    else:
        print("Invalid Input!")

    