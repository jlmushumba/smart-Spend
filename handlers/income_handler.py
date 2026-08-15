import json
from datetime import datetime
from services.income_service import add_income_parameters, delete_income, edit_income
from utils.menu import income_menu
from services.income_service import (add_income, view_income)


def handle_income():
    print(income_menu())

    while True:
        choice_income = input(">>")

        if choice_income == "1": # add new income

            income_id, source , amount, date, description = add_income_parameters()
            add_income(income_id, source , amount, date, description)
            print(income_menu())

        elif choice_income == "2": # view all incomes
            try:
                incomes = view_income()
            
                if not incomes:
                    print(income_menu())
                elif incomes:
                    for income in incomes:
                        print("=" * 45)
                        for key, value in income.items():
                            print(f"{key}: {value}")
                        print()
                        print("=" * 45)
            except Exception as error:
                print(f"No incomes found!")
            
            

        elif choice_income == "3": # delete income
            # display all incomes

            incomes = view_income()
            try:
                for income in incomes:
                    print("=" * 45)
                    for key, value in income.items():
                        print(f"{key}: {value}")
                    print()
                    print("=" * 45)


                    while True:

                        try:

                            id_to_delete = int(input("Enter ID for income to delete: "))
                            break
                        except ValueError:
                            print("Please enter a valid income ID!")
                        delete_income(id_to_delete)
                        print(income_menu())

            except Exception:
                print("No incomes found to delete!")
                print(income_menu())

            
        elif choice_income == "4":
            # TODO "
            # implement edit_income function"
            try:
                with open ("income.json", "r") as file:
                    data = json.load(file)
                    if data:
                        while True:

                            try:

                                edit_id = int(input("Enter income ID to edit: "))
                                break
                            except ValueError:
                                print("Invalid input!")
                            except Exception as error:
                                print(f"Error: {error}")

                        
                        
                        edit_choices = {}
                        while True:
                            print("What do you want to change ?")
                            print("1. Source \n 2. Amount \n 3. Date \n 4. Description \n 5. Complete")
                            edit_choice = (input(">> "))
                                    
                        
                            if edit_choice == "1":
                                edit_choices['source'] = input("Enter new source: ")
                            elif edit_choice == "2":

                                while True:
                                        try:
                                            new_amount = int(input("Enter new amount: "))
                                            if  new_amount < 0:
                                                print("Amount cannot be negative.")
                                                continue
                                            edit_choices['amount'] = new_amount
                                            break
                                        except ValueError:
                                            print("Invalid input! Please enter a valid number.")
                                
                            elif edit_choice == "3":
                                while True:
                                        
                                        try:
                                            new_date = input("Enter new date (DD/MM/YYYY): ")
                                            datetime.strptime(new_date, "%d/%m/%Y")
                                            edit_choices['date'] = new_date
                                            break
                                        except ValueError:
                                            print("Invalid date format! Please enter in DD/MM/YYYY format (e.g., 10/08/2026).")
                                
                            elif edit_choice == "4":
                                edit_choices['description'] = input("Enter new Description: ")

                            elif edit_choice == "5":
                                edit_income(edit_choices, edit_id)
                                print(income_menu())
                                break
                            
                            else:
                                print("Invalid option! Please enter a number from 1 to 5.")

                        
            except Exception:
                print("No editable incomes found!")
                print(income_menu())
            
            
        elif choice_income == "5":
            break # here we are returning to the main menu

        else:
            print("Invalid input!")
            print(income_menu())