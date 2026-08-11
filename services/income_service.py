from models.income import Income
import json

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
    pass

def delete_income():
    pass
