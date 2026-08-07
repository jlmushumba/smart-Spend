# Displaying the banner and the menu
from utils.helpers import read_file, edit_profile_data
import sys
from services.user_service import (create_profile, view_profile,edit_profile)
from utils.menu import (
    main_menu, user_profile_menu, income_menu, expenses_menu, budget_menu, reports_menu
    )

print(read_file("assets/logo.txt"))

while True:

    
    print(main_menu())

    choice = input(">> ")

    if choice == "1":
        print(user_profile_menu())

        choice = input(">>")

        if choice == "1":

            name = input("Enter your name: ")
            email = input("Enter your email: ")
            currency = input("Enter the desired currency: ")
            create_profile(name, email, currency)
            print("Profile created succesflly!")

        elif choice == "2":
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

        elif choice == "3":
            data = edit_profile_data()
            edit_profile(data)
                
        else:
            print("Invalid option!!!")

    elif choice == "2":
        print("Feature coming soon...")

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
