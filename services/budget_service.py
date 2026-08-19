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


def edit_budget():
    
    pass

def delete_budget():
    pass