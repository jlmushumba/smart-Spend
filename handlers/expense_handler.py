import json
from datetime import datetime
from services.expense_service import add_expense_parameters, delete_expense, edit_expense
from utils.menu import expenses_menu
from services.expense_service import (add_expense, view_expense)


def handle_expense():
    print(expenses_menu())

    while True:
        choice_expense = input(">>")

        if choice_expense == "1": # add new expense

            expense_id, category , amount, date, description = add_expense_parameters()
            add_expense(expense_id, category , amount, date, description)
            print(expenses_menu())

        elif choice_expense == "2": # view all expenses
            try:
                expenses = view_expense()
            
                if not expenses:
                    print("No expenses found!")
                    print(expenses_menu())
                elif expenses:
                    for expense in expenses:
                        print("=" * 45)
                        for key, value in expense.items():
                            print(f"{key}: {value}")
                        print()
                        print("=" * 45)
                    print(expenses_menu())
            except Exception as error:
                print(f"No expenses found!")

            
            

        elif choice_expense == "3": # delete expense
            # display all expenses

            expenses = view_expense()
            if not expenses:
                print("No expenses found to delete!")
                print(expenses_menu())
            else:
                for expense in expenses:
                    print("=" * 45)
                    for key, value in expense.items():
                        print(f"{key}: {value}")
                    print()
                    print("=" * 45)


                while True:

                    try:

                        id_to_delete = int(input("Enter ID for expense to delete: "))
                        
                        break
                    except ValueError:
                        print("Please enter a valid expense ID!")
                        
                delete_expense(id_to_delete)
                print(expenses_menu())


            
        elif choice_expense == "4":
            # TODO "
            # implement edit_expense function"
            try:
                with open ("data/expenses.json", "r") as file:
                    data = json.load(file)
                    if data:
                        while True:

                            try:

                                edit_id = int(input("Enter expense ID to edit: "))
                                break
                            except ValueError:
                                print("Invalid input!")
                            except Exception as error:
                                print(f"Error: {error}")

                        
                        
                        edit_choices = {}
                        while True:
                            print("What do you want to change ?")
                            print("1. Category \n 2. Amount \n 3. Date \n 4. Description \n 5. Complete")
                            edit_choice = (input(">> "))
                                    
                        
                            if edit_choice == "1":
                                edit_choices['category'] = input("Enter new category: ")
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
                                edit_expense(edit_choices, edit_id)
                                print(expenses_menu())
                                break
                            
                            else:
                                print("Invalid option! Please enter a number from 1 to 5.")

                        
            except Exception:
                print("No editable expenses found!")
                print(expenses_menu())
            
            
        elif choice_expense == "5":
            break # here we are returning to the main menu

        else:
            print("Invalid input!")
            print(expenses_menu())

