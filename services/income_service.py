from models.income import Income
import json
from datetime import datetime

def add_income(id, source, amount, date, description):

    try:
        income = Income(id, source, amount, date, description)
        data = income.to_dict()

        try:
            

            with open ("data/income.json", "r") as file:
                incomes = json.load(file)

        except FileNotFoundError as error1:
            print(f"Error: {error1}")
        except json.decoder.JSONDecodeError:
            incomes = []

        incomes.append(data)

        with open("data/income.json", "w") as file:
            json.dump(incomes, file, indent=4)

    except Exception as error:
        print(f"Error: {error}")



def view_income():
    try:

        with open ("data/income.json", "r") as file:
            incomes = json.load(file)
           
    except FileNotFoundError:
        print("Error: income data is missing!")
    except Exception as error:
        print(f"Error: {error}")

    return incomes

def edit_income():
    # TODO "
    # - ask what the user want to change. store it into the list
    # - Iterate over a dictionary and then change the variable 
    # - but first make sure that it is a error free variable"
    
    pass

def delete_income(id_to_delete):
    """
    This function help you delete an income by its ID 
    """

    try:

        with open ("data/income.json", "r") as file:
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


# intra helper function

def recent_id():
    """
    Return recent ID in data/income.json file
    """
    with open ("data/income.json", "r") as file:
        incomes = json.load(file)

    if incomes:
        recent_id = incomes[-1]['id']
    else:
        recent_id = 0

    return recent_id



# Intra helper function

def add_income_parameters():
    """
    This function collects essential parameters for 
    add_income() function in "services/income_service.py" 
    wich wil be used in main.py
    """

    # id

    

    income_id = recent_id() + 1

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

