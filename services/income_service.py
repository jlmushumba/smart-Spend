from models.income import Income
import json

def add_income(data):
    try:
        with open ("data/income.json", "a") as file:
            json.dump(data, file, indent=4)

    except FileNotFoundError as error:
        print(f"Error: {error}")
    except Exception:
        print(f"Error: {error}")



def view_income():
    try:

        with open ("data/income.json", "r") as file:
            incomes = json.load(file)
            return incomes
    except FileNotFoundError:
        print("Error: income data is missing!")
    except Exception as error:
        print(f"Error: {error}")

def edit_income():
    pass

def delete_income():
    pass
