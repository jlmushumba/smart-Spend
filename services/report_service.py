import json
expense_file = "data/expenses.json"
income_file = "data/income.json"

# Expenses part

def total_expenses():
 

    try:

        with open(expense_file, "r") as file:
            expenses = json.load(file)
        total_expenses = 0
        for expense in expenses:
            total_expenses += expense["amount"]

    except FileNotFoundError as e1:
        print(f"Error: {e1}")
        return False
    except json.JSONDecodeError as e2:
        print(f"Error: {e2}")
        return False
    except Exception as e3:
        print(f"Error: {e3}")
        return False
    return total_expenses

def total_income():
  
    
    try:

        with open(income_file, "r") as file:
            incomes = json.load(file)
        total_income = 0
        for income in incomes:
            total_income += income["amount"]
        
    except FileNotFoundError as e1:
        print(f"Error: {e1}")
        return False
    except json.JSONDecodeError as e2:
        print(f"Error: {e2}")
        return False
    except Exception as e3:
        print(f"Error: {e3}")
        return False
    return total_income
    

def balance():
    income = total_income()
    if income is False:
        return False
    expense = total_expenses()
    if expense is False:
        return False
    balance = income - expense

    return balance
    

if __name__ == "__main__":
    print(total_expenses())
    print(total_income())
    print(balance())