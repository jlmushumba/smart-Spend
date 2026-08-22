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

def number_of_expenses():

    try:

        with open(expense_file, "r") as file:
            expenses = json.load(file)
        return len(expenses)
    except FileNotFoundError as e1:
            print(f"Error: {e1}")
            return False
    except json.JSONDecodeError as e2:
        print(f"Error: {e2}")
        return False
    except Exception as e3:
        print(f"Error: {e3}")
        return False 


def highest_expense():
    try:

        with open (expense_file, "r") as file:
            expenses = json.load(file)

        if not expenses:
            return False
        highest = expenses[0]

        for expense in expenses:

            if expense["amount"] > highest["amount"]:
                highest = expense

        return highest

        

    except FileNotFoundError as e1:
        print(f"Error: {e1}")
        return False
    except json.JSONDecodeError as e2:
        print(f"Error: {e2}")
        return False
    except Exception as e3:
        print(f"Error: {e3}")
        return False
def total_income():
  
    
    try:

        with open(income_file, "r") as file:
            incomes = json.load(file)
        if incomes:

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
    
def number_of_incomes():
    try: 
        with open(income_file, "r") as file:
            incomes = json.load(file)
        return len(incomes)
    except FileNotFoundError as e1:
        print(f"Error: {e1}")
        return False
    except json.JSONDecodeError as e2:
        print(f"Error: {e2}")
        return False
    except Exception as e3:
        print(f"Error: {e3}")
        return False

def highest_income():
    try:

        with open (income_file, "r") as file:
            incomes = json.load(file)

        if not incomes:
            return False
        highest = incomes[0]

        for income in incomes:

            if income["amount"] > highest["amount"]:
                highest = income

        return highest
    except FileNotFoundError as e1:
        print(f"Error: {e1}")
        return False
    except json.JSONDecodeError as e2:
        print(f"Error: {e2}")
        return False
    except Exception as e3:
        print(f"Error: {e3}")
        return False

def balance():
    income = total_income()
    if income is False:
        return False
    expense = total_expenses()
    if expense is False:
        return False
    balance = income - expense

    return balance

def savings_rate():
    ti = total_income()
    bal = balance()

    # Guard against invalid boolean returns or 0 total income
    if not isinstance(ti, (int, float)) or ti <= 0:
        return 0.0
    if not isinstance(bal, (int, float)):
        return 0.0

    return (bal / ti) * 100


if __name__ == "__main__":
    print(total_expenses())
    print(total_income())
    print(balance())
    print(number_of_expenses())
    print(number_of_incomes())
    print(highest_expense())
    print(highest_income())
    print(savings_rate())