import json
from datetime import datetime
from models.budget import Budget

file_path = "data/budgets.json"

def add_budget(id: int, category: str, monthly_limit: int, month_year: datetime):

    budget = Budget(id, category, monthly_limit, month_year)
    budget_data = budget.to_dict()
    try:

        with open(file_path, "r") as file:
            budgets = json.load(file)
    except FileNotFoundError as e1:
        print(f"Error(add_budget): {e1}")
    except json.JSONDecodeError as e2:
        budgets = []

    budgets.append(budget_data)

    with open (file_path, "w") as file:
        json.dump(budgets, file, indent=4)

def view_budget():

    try:

        with open (file_path, "r") as file:
            budgets = json.load(file)
            return budgets
    except FileNotFoundError as e1:
        print(f"Error: {e1}")
    except json.JSONDecodeError as e2:
        print(f"Error: {e2}")


def edit_budget(edit_choices: dict, edit_id: int):

    try:

        with open (file_path, "r") as file:
            budgets = json.load(file)

        for budget in budgets:
            if budget['id'] == edit_id:
                for key, value in edit_choices.items():
                    budget[key] = value


        with open (file_path, "w") as file:
            json.dump(budgets, file, indent=4)
        
    except FileNotFoundError as e1:
        print(f"Error: {e1}")
    except json.JSONDecodeError as e2:
        print(f"Error: {e2}")
    except Exception as e3:
        print(f"Error: {e3}")

def delete_budget(id_to_delete):
    try:

        with open (file_path, "r") as file:
            budgets = json.load(file)

            updated_budgets = [budget for budget in budgets if budget.get("id") != id_to_delete]
            if len(updated_budgets) == len(budgets):
                print(f"Budget with Income ID {id_to_delete} was not deleted!")
                return False
        with open(file_path, "w") as file:
            json.dump(updated_budgets, file, indent=4)
        print(f"Budget with ID {id_to_delete} was deleted successfully!")
        return True

    
    except FileNotFoundError as e1:
        print(f"Error: {e1}")
    except json.JSONDecodeError as e2:
        print(f"Error: {e2}")
    except Exception as e3:
        print(f"Error: {e3}")

    