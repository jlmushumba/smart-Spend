# Displaying the banner and the menu
from utils.helpers import read_file, edit_profile_data, add_income_parameters
import sys
from services.user_service import (create_profile, view_profile,edit_profile)
from utils.menu import (
    main_menu, user_profile_menu, income_menu, expenses_menu, budget_menu, reports_menu
    )
from services.income_service import (add_income, view_income)

print(read_file("assets/logo.txt"))

while True:


    print(main_menu())

    choice = input(">> ")

    if choice == "1":
        
        print(user_profile_menu())
        while True:
            choice_user = input(">>")
        
            if choice_user == "1":

                name = input("Enter your name: ")
                email = input("Enter your email: ")
                currency = input("Enter the desired currency: ")
                create_profile(name, email, currency)
                print("Profile created succesfully!")
                print(user_profile_menu())
                

            elif choice_user == "2":
                try:

                    profile = view_profile()
                except Exception as e:
                    print(f"Error: No profile found!")

                else:

                    print(f"""
                    
                        Name: {profile["name"]}\n
                        Email: {profile["email"]}\n
                        Currency: {profile["currency"]}\n
                        """
                    )
                    print(user_profile_menu())

            elif choice_user == "3":
                data = edit_profile_data()
                edit_profile(data)
                print(user_profile_menu())

            elif choice_user == "4":
                break
            else:
                print("Invalid option!!!")
            

    elif choice == "2":

        print(income_menu())

        while True:
            choice_income = input(">>")

            if choice_income == "1":
                income_id, source , amount, date, description = add_income_parameters()
                add_income(income_id, source , amount, date, description)
                print(income_menu())

            elif choice_income == "2":
                
                incomes = view_income()
                for income in incomes:
                    print("=" * 45)
                    for key, value in income.items():
                        print(f"{key}: {value}")
                    print()
                    print("=" * 45)
                print(income_menu())

            elif choice_income == "3":
                pass

            elif choice :
                pass

    elif choice == "3":
        print("Feature coming soon...")

    elif choice == "4":
        print("Feature coming soon...")

    elif choice == "5":
        print("Feature coming soon...")

    elif choice == "6":
        print("Closing Smart Spend...")
        sys.exit()
        

    else:
        print("Invalid option")
        sys.exit()
