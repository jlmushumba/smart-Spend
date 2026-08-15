from services.user_service import edit_profile_data
from services.user_service import (create_profile, view_profile,edit_profile)
from utils.menu import user_profile_menu


def handle_user_profile():
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
                print(user_profile_menu())

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
            print(user_profile_menu())