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

def add_income_parameters():
    """
    This function collects essential parameters for 
    add_income() function in "services/income_service.py" 
    wich wil be used in main.py
    """

    # id

    try:

        with open ("data/income.json", "r") as file:
            income_data = json.load(file)
            if income_data:
                income_id = income_data[-1]["id"] + 1
            #else:
                #income_id = 1
    except FileNotFoundError:
        print("System Error!")
    except json.decoder.JSONDecodeError:
        income_id = 1

    #source
    income_source = input("Enter income source: ")

    #amount

    while True:
        try:
            income_amount = float(input("Enter amount in digits: "))
            if income_amount < 0:
                print("Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    #date
    while True:
        income_date = input("Enter date(DD/MM/YYYY): ")
        try:

            date_object = datetime.strptime(income_date, "%d/%m/%Y").date()
            formatted_date = date_object.strftime("%d/%m/%Y")
            income_date =formatted_date
            break
        except ValueError:
            print("Invalid date format! Please enter in DD/MM/YYYY format (e.g., 10/08/2026).")
    # description

    income_description = input("Enter income short description: ")


    return income_id, income_source, income_amount, income_date, income_description

# delete income by ID helper function

def delete_income(id_to_delete):
    """
    This function help you delete an income by its ID 
    """

    try:

        with open ("data/income.json", "r+") as file:
            incomes = json.load(file)

            updated_incomes = [income for income in incomes if income.get('id') != id_to_delete]

            if len(updated_incomes) == len(incomes):
                print(f"Income with Income ID {id_to_delete} was not deleted!")
                return False

        with open("data/income.json", "w") as file:
            json.dump(updated_incomes, file, indent=4)
        print(f"Income with ID {id_to_delete} was deleted successfully!")
        return True
        
        
    except FileNotFoundError:
        print("Incomes are not found!")
    except json.JSONDecodeError:
        print("No incomes found!")
    except Exception as error:
        print(f"Error: {error}")