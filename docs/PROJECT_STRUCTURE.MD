# Project Structure Explanation

## Overview

The SmartSpend project follows a modular directory structure based on the principle of separating responsibilities. Each folder is responsible for one part of the application, making the project easier to understand, maintain, test, and extend.

---

# Root Directory

The root directory contains the main application files and all project modules.

```text
SmartSpend/
```

---

# assets/

Contains all text-based visual resources displayed in the terminal application.

## Files

### `banner.txt`

Displays the large welcome banner shown when the application starts.

**Example:**

```text
==================================
        SMARTSPEND
 Personal Budget Management System
==================================
```

### `logo.txt`

Stores the application's ASCII logo used throughout the program.

---

# data/

Acts as the application's database.

Since SmartSpend is a beginner project, information is stored in JSON files instead of a relational database.

## Files

### `budgets.json`

Stores every budget created by the user.

**Example**

```json
[
    {
        "category": "Food",
        "limit": 50000
    }
]
```

### `expenses.json`

Stores all expense records.

### `income.json`

Stores all income records.

### `profile.json`

Stores user information such as:

- Name
- Preferred currency
- Monthly salary
- Savings goal

### `settings.json`

Stores application settings including:

- Theme
- Notifications
- Default report options

---

# docs/

Contains all project documentation.

This folder helps developers and users understand how the application works.

## Files

### `DESIGN.md`

Explains:

- Software architecture
- Module relationships
- Class diagrams
- Design decisions

### `SRS.md`

Software Requirements Specification.

Contains:

- Functional requirements
- Non-functional requirements
- Assumptions
- Project scope

### `USER_GUIDE.md`

User manual explaining:

- Installation
- Running the program
- Navigating menus
- Examples

### `screenshots/`

Stores screenshots used inside the documentation.

**Examples**

```text
Main_Menu.png
Budget_Menu.png
Expense_Report.png
```

---

# main.py

The application's entry point.

### Responsibilities

- Launches the application
- Displays the main menu
- Connects all services together
- Controls program navigation

Think of it as the application's controller.

---

# models/

Contains all data models.

Models describe what a piece of data looks like.

Each model usually represents one real-world object.

## Files

### `budget.py`

Defines the **Budget** model.

Example attributes:

```python
category
limit
month
```

### `expense.py`

Defines the **Expense** model.

Example attributes:

```python
amount
category
date
description
```

### `income.py`

Defines the **Income** model.

Example attributes:

```python
amount
source
date
```

### `user.py`

Represents the application's user profile.

Example attributes:

```python
name
currency
monthly_income
```

### `__init__.py`

Marks the folder as a Python package.

Allows imports like:

```python
from models import Budget
```

---

# reports/

Stores generated reports.

Instead of mixing generated files with source code, reports are organized separately.

## Subdirectories

### `monthly/`

Contains monthly reports.

**Examples**

```text
January_2026.txt
February_2026.txt
```

### `yearly/`

Contains yearly financial summaries.

**Example**

```text
2026_Report.txt
```

---

# requirements.txt

Lists external Python libraries required by the project.

**Example**

```text
tabulate
colorama
```

Install them using:

```bash
pip install -r requirements.txt
```

---

# services/

Contains the application's business logic.

Services perform operations using the models and stored data.

Think of services as the **brains** of the application.

## Files

### `budget_service.py`

Handles:

- Creating budgets
- Updating budgets
- Deleting budgets
- Checking budget limits

### `expense_service.py`

Handles:

- Adding expenses
- Deleting expenses
- Listing expenses
- Expense calculations

### `income_service.py`

Handles:

- Recording income
- Updating income
- Income summaries

### `report_service.py`

Generates:

- Monthly reports
- Yearly reports
- Spending summaries
- Savings reports

### `search_service.py`

Provides searching functionality.

Examples:

- Search expenses
- Search income
- Search by category
- Search by date

### `user_service.py`

Manages:

- User profile
- Settings
- Preferences

### `__init__.py`

Marks the directory as a Python package.

---

# storage/

Responsible for reading and writing files.

This separates storage logic from business logic.

## Files

### `file_manager.py`

Handles:

- Creating folders
- Checking file existence
- Reading files
- Writing files

### `json_handler.py`

Handles all JSON operations.

Examples:

```python
load_data()

save_data()

update_data()
```

### `__init__.py`

Marks the directory as a package.

---

# tests/

Contains automated unit tests.

Testing ensures every feature works correctly.

## Files

### `test_budget.py`

Tests budget features.

### `test_expense.py`

Tests expense functions.

### `test_income.py`

Tests income features.

### `test_search.py`

Tests search functionality.

### `test_storage.py`

Tests JSON loading and saving.

### `__init__.py`

Marks the folder as a package.

---

# utils/

Contains reusable helper functions used throughout the project.

Utilities avoid repeating code.

## Files

### `constants.py`

Stores application constants.

Examples:

```python
MAX_BUDGET

DEFAULT_CURRENCY

APP_NAME
```

### `formatter.py`

Formats output for display.

Examples:

- Currency formatting
- Table formatting
- Date formatting

### `helpers.py`

General helper functions shared across modules.

Examples:

```python
clear_screen()

pause()

print_header()
```

### `menu.py`

Displays application menus.

Example:

```text
Main Menu
Budget Menu
Expense Menu
```

### `validator.py`

Validates user input.

Examples:

- Numbers
- Dates
- Currency
- Menu choices

### `__init__.py`

Marks the directory as a package.

---

# utilsreports/

Provides helper utilities specifically for report generation.

Unlike the `reports/` directory, which stores generated output, this folder contains reusable code or templates that support reporting.

Possible responsibilities include:

- Report templates
- Report formatting utilities
- Export helpers
- Chart or statistics helpers
- Common report calculations

Keeping reporting utilities separate improves organization and prevents report-generation logic from becoming tightly coupled with the main application.

---

# Overall Architecture

```text
                 main.py
                     │
         ┌───────────┼───────────┐
         │           │           │
     services     utils      storage
         │           │           │
         │           │      JSON Files
         │           │           │
         ├───────────┘           │
         │                       │
      models                 data/
         │
         └──────────────► reports/
```

---
