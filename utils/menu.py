def main_menu():
    with open ("assets/main_menu.txt", "r") as file:
        menu = file.read()
        return menu


def user_profile_menu():
    with open ("assets/user_profile.txt", "r") as file:
        user_profile = file.read()
        return user_profile
    

def income_menu():
    with open ("assets/income_menu.txt", "r") as file:
        income_menu_display = file.read()
        return income_menu_display
    

def expenses_menu():
    with open ("assets/expenses_menu.txt", "r") as file:
            expense_menu_display = file.read()
            return expense_menu_display

def budget_menu():
    pass

def reports_menu():
    pass

if __name__ == "__main__":

    print(user_profile_menu())