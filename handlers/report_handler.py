from pathlib import Path
from utils.menu import reports_menu
from services.report_service import (
    total_expenses, 
    number_of_expenses, 
    highest_expense, 
    total_income, 
    number_of_incomes, 
    highest_income, 
    balance,
    savings_rate
    
)

from utils.helpers import format_record

REQUIRED_FILES = [
    "data/budgets.json",
    "data/expenses.json",
    "data/income.json",
    "data/profile.json"
]

def are_all_files_ready() -> bool:
    """Returns True ONLY if all required data files exist and are not empty."""
    for file_path in REQUIRED_FILES:
        path = Path(file_path)
        # Check if file exists and has a byte size greater than 0
        if not path.exists() or path.stat().st_size == 0:
            print(f"[!] Warning: Missing or empty file detected: {file_path}")
            return False
    return True


def report_handler():

    if not are_all_files_ready():
        print("\n[X] Error: Cannot generate reports. One or more data files are empty or missing.")
        print("Please ensure entries exist in Income, Expenses, Budgets, and Profile first.\n")
        return  # Exits back to main menu cleanly

    
    te = total_expenses()
    ti = total_income()
    ne = number_of_expenses()
    he = highest_expense()
    ni = number_of_incomes()
    hi = highest_income()
    b = balance()
    sr = savings_rate()

    highest_income_details = format_record(hi) if isinstance(hi, dict) else "  No income data found."
    highest_expense_details = format_record(he) if isinstance(he, dict) else "  No expense data found."



    complete_report = f"""
    ========================================
            SMARTSPEND REPORT
    ========================================

    Period: All Time

    INCOME
    ----------------------------------------
    Total Income:              {ti}
    Number of Income Records:  {ni}
    Highest Income:
    {highest_income_details}
    ----------------------------------------

    EXPENSES
    ----------------------------------------
    Total Expenses:            {te}
    Number of Expense Records: {ne}
    Highest Expense:
    {highest_expense_details}
    ----------------------------------------

    FINANCIAL SUMMARY
    ----------------------------------------
    Total Income:              {ti}
    Total Expenses:            {te}
    Balance:                   {b}

    Savings Rate:              {sr}%
    ========================================
    """

    print(reports_menu())

    while True:

        choice = input(">> ")

        if choice == "1":

            print(complete_report)

        elif choice == "2":
            break
            
        else:
            print("Invalid input!")
            print(reports_menu())

