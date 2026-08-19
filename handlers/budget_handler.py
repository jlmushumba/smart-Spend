from datetime import datetime
from utils.menu import budget_menu
from services.budget_service import (
    add_budget, view_budget, edit_budget, delete_budget
)
from utils.helpers import recent_id

def handle_budget():

    print(budget_menu())

    while True:

        budget_choice = input(">> ")

        if budget_choice == "1": # set budget

            # id 
            id = recent_id("data/budgets.json")

            # category

            category = input("Enter category: ")

            # monthly limit money

            while True:
                try:

                    monthly_limit = int(input("Enter money monthly limit: "))
                    break
                except ValueError:
                    print("Please enter a valid amount of money in numbers!")
                except Exception as error:
                    print(f"Error: {error}")

            # month/year of setting the monthly budget

            while True:
                budget_date = input("Enter budget month (MM/YYYY): ")
                try:
                                                           
                    date_object = datetime.strptime(budget_date, "%m/%Y").date()
                    formatted_date = date_object.strftime("%m/%Y")
                    month_year = formatted_date
                    break
                 
                except ValueError:
                    print("Invalid date format! Please enter in MM/YYYY format (e.g., 08/2026)")
                except Exception as e1:
                    print(f"Error: {e1}")

            add_budget(id, category, monthly_limit, month_year)
            print(budget_menu())
           

        elif budget_choice == "2": # view budget
            budgets = view_budget()

            for budget in budgets:
                print("=" * 45)
                for key, value in budget.items():
                    print(f"{key} : {value}")
            
            print(budget_menu())

        elif budget_choice == "3": # edit budget by ID
            edit_budget()
            pass

        elif budget_choice == "4": # Delete budget by ID
            delete_budget()
            

        elif budget_choice == "5": # back to main menu
            break
        