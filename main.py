# Displaying the banner and the menu
from utils.helpers import read_file
import sys
from utils.menu import main_menu
from handlers.user_handler import handle_user_profile
from handlers.income_handler import handle_income
from handlers.expense_handler import handle_expense
from handlers.budget_handler import handle_budget
print(read_file("assets/logo.txt"))

while True:


    print(main_menu())

    choice = input(">> ")

    if choice == "1":
        # user handler
        handle_user_profile()
    
    elif choice == "2":
        # income handler
        handle_income()
        
    elif choice == "3":
        handle_expense()

    elif choice == "4":
        handle_budget()

    elif choice == "5":
        print("Feature coming soon...")

    elif choice == "6":
        print("Closing Smart Spend...")
        sys.exit()
        

    else:
        print("Invalid option")
        sys.exit()
