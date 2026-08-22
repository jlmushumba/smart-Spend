from models.expense import Expense
import json
from datetime import datetime

def add_expense(id, category, amount, date, description):

    try:
        expense = Expense(id, category, amount, date, description)
        data = expense.to_dict()

        try:
            

            with open ("data/expenses.json", "r") as file:
                expenses = json.load(file)

        except FileNotFoundError as error1:
            print(f"Error: {error1}")
        except json.decoder.JSONDecodeError:
            expenses = []

        expenses.append(data)

        with open("data/expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

    except Exception as error:
        print(f"Error: {error}")



def view_expense():
    try:

        with open ("data/expenses.json", "r") as file:
            expenses = json.load(file)
            return expenses
           
    except FileNotFoundError:
        print("Error: expense data is missing!")
    except Exception as error:
        print("No expenses found!")
        return None
    

def edit_expense(edit_choices: dict, edit_id: int):
    # TODO "
    # - ask what the user want to change. store it into the list
    # - Iterate over a dictionary and then change the variable 
    # - but first make sure that it is a error free variable
    # - make it possible to edit multiple inputs in one go"

    try:

        with open ("data/expenses.json" ,"r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        print("Expenses are not found!")
    except json.JSONDecodeError as e:
        print("Zero expenses found!")
        print(f"JSONDecodeError: {e}")    
    except Exception as error:
        print(f"Error: {error}")    


    for expense in expenses:
        if expense['id'] == edit_id:
            for key, value in edit_choices.items():
                expense[key] = value


    try:

        with open ("data/expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

    except FileNotFoundError:
        print("Expenses are not found!")
    except json.JSONDecodeError as e:
        print("Zero expenses found!")
        print(f"JSONDecodeError: {e}")    
    except Exception as error:
        print(f"Error: {error}")
    
def delete_expense(id_to_delete):
    """
    This function help you delete an expense by its ID 
    """

    try:

        with open ("data/expenses.json", "r") as file:
            expenses = json.load(file)

            updated_expenses = [expense for expense in expenses if expense.get('id') != id_to_delete]


            if len(updated_expenses) == len(expenses):
                print(f"Expense with Expense ID {id_to_delete} was not deleted!")
                return False

        with open("data/expenses.json", "w") as file:
            json.dump(updated_expenses, file, indent=4)
        print(f"Expense with ID {id_to_delete} was deleted successfully!")
        return True
        
        
    except FileNotFoundError:
        print("Expenses are not found!")
    except json.JSONDecodeError:
        print("No expenses found!")
    except Exception as error:
        print(f"Error: {error}")


# intra helper function

def recent_id():
    """
    Return recent ID in data/expenses.json file
    """
    try:

        with open ("data/expenses.json", "r") as file:
            expenses = json.load(file)
            if expenses:
                    recent_id = expenses[-1]['id']
            else:
                    recent_id = 0
            #recent_id = expenses[-1]['id']
    except FileNotFoundError as error:
        print(f"Error: {error}")
    except json.JSONDecodeError:
        recent_id = 0

    

    return recent_id



# Intra helper function

def add_expense_parameters():
    """
    This function collects essential parameters for 
    add_expense() function in "services/expense_service.py" 
    wich wil be used in main.py
    """

    # id

    

    expense_id = recent_id() + 1

    #category
    expense_category = input("Enter expense category: ")

    #amount

    while True:
        try:
            expense_amount = float(input("Enter amount in digits: "))
            if expense_amount < 0:
                print("Amount cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    #date
    while True:
        expense_date = input("Enter date(DD/MM/YYYY): ")
        try:

            date_object = datetime.strptime(expense_date, "%d/%m/%Y").date()
            formatted_date = date_object.strftime("%d/%m/%Y")
            expense_date =formatted_date
            break
        except ValueError:
            print("Invalid date format! Please enter in DD/MM/YYYY format (e.g., 10/08/2026).")
    # description

    expense_description = input("Enter expense short description: ")


    return expense_id, expense_category, expense_amount, expense_date, expense_description

# delete expense by ID helper function




