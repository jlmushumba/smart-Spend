# Displaying the banner and the menu
from utils import helpers
import sys

while True:

    print(helpers.read_file("assets/logo.txt"))
    print(helpers.read_file("assets/banner.txt"))

    choice = input(">> ")

    if choice == "1":
        print("Feature coming soon...")
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
