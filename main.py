# Displaying the banner and the menu
from utils import helpers
import sys
from services.user_service import create_profile, view_profile


while True:

    print(helpers.read_file("assets/logo.txt"))
    print(helpers.read_file("assets/banner.txt"))

    choice = input(">> ")

    if choice == "1":
        print(helpers.read_file("assets/user_profile.txt"))

        choice = input(">>")

        if choice == "1":

            name = input("Enter your name: ")
            email = input("Enter your email: ")
            currency = input("Enter the desired currency: ")
            create_profile(name, email, currency)
            print("Profile created succesflly!")

        elif choice == "2":
            profile = view_profile()
            print(f"""
            
                Name: {profile["name"]}\n
                Email: {profile["email"]}\n
                Currency: {profile["currency"]}\n
                """
            )

        elif choice == "3":
            print("Feature coming soon..")
                
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
