# Software Requirements Specification (SRS)

# SmartSpend: Personal Finance Manager

**Version:** 1.0  
**Prepared By:** Jean Louange MUSHUMBA  
**Date:** August 2026

---

# Table of Contents

1. Introduction
2. Overall Description
3. Functional Requirements
4. Non-Functional Requirements
5. System Architecture
6. Data Storage
7. Assumptions
8. Limitations
9. Future Enhancements

---

# 1. Introduction

## 1.1 Purpose

SmartSpend is a command-line Personal Finance Manager developed in Python to help users monitor and manage their finances. The application enables users to record income and expenses, manage budgets, and generate financial reports using locally stored data.

The project is intended as an educational software engineering project that demonstrates programming fundamentals, object-oriented design, modular development, and file handling without relying on external databases or internet connectivity.

---

## 1.2 Scope

The application allows users to:

- Create and manage a personal profile
- Record income
- Record expenses
- Categorize transactions
- Set monthly budgets
- Generate financial summaries
- Search financial records
- Store information locally using JSON files

The application operates entirely offline through a terminal interface.

---

## 1.3 Objectives

The objectives of SmartSpend are to:

- Help users understand their spending habits.
- Encourage responsible budgeting.
- Provide an easy-to-use finance management tool.
- Demonstrate software engineering best practices.
- Strengthen Python programming skills.

---

## 1.4 Intended Users

SmartSpend is designed for:

- Students
- Beginners learning Python
- Individuals managing personal finances
- Software engineering learners

---

## 1.5 Definitions

| Term | Meaning |
|------|---------|
| CLI | Command Line Interface |
| JSON | JavaScript Object Notation used for local storage |
| Income | Money earned |
| Expense | Money spent |
| Budget | Planned spending limit |
| Transaction | Income or Expense record |

---

# 2. Overall Description

## 2.1 Product Perspective

SmartSpend is a standalone desktop application executed from the command line.

The application:

- Runs completely offline.
- Uses JSON for persistent storage.
- Does not require a database.
- Does not require internet connectivity.
- Supports a single user.

---

## 2.2 Product Features

The system provides the following modules:

### User Profile

- Create profile
- View profile
- Update profile

### Income Management

- Add income
- View income
- Edit income
- Delete income

### Expense Management

- Add expense
- View expenses
- Edit expense
- Delete expense
- Search expenses

### Budget Management

- Set monthly budget
- Update budget
- Monitor remaining budget

### Reports

- Total income
- Total expenses
- Current balance
- Spending by category
- Monthly summaries
- Largest expense

### Data Storage

- Automatic saving
- Automatic loading
- JSON persistence

---

## 2.3 User Characteristics

Users are expected to have:

- Basic computer knowledge
- Basic terminal usage
- No programming knowledge required

---

## 2.4 Operating Environment

Operating Systems:

- Ubuntu Linux
- Windows
- macOS

Programming Language:

- Python 3.10+

Storage:

- JSON files

---

## 2.5 Constraints

The application shall:

- Use Python only.
- Operate from the terminal.
- Use Object-Oriented Programming.
- Store data using JSON.
- Follow PEP 8 coding standards.
- Avoid external frameworks.

---

# 3. Functional Requirements

## FR1 User Profile

The system shall allow users to:

- Create a profile
- Update profile information
- View profile

### Profile Information

- Name
- Email
- Preferred Currency
- Monthly Income Goal

---

## FR2 Income Management

The system shall allow users to:

- Add income
- View all income
- Edit income
- Delete income

### Income Fields

- Income ID
- Source
- Amount
- Date
- Description

---

## FR3 Expense Management

The system shall allow users to:

- Add expenses
- View expenses
- Edit expenses
- Delete expenses
- Search expenses

### Expense Fields

- Expense ID
- Title
- Amount
- Category
- Date
- Description

---

## FR4 Categories

The system shall support predefined categories:

- Food
- Transport
- Housing
- Utilities
- Shopping
- Entertainment
- Healthcare
- Education
- Savings
- Other

---

## FR5 Budget Management

The system shall allow users to:

- Set monthly budgets
- Modify budgets
- View remaining budget
- Display overspending warnings

---

## FR6 Reports

The system shall generate reports including:

- Total Income
- Total Expenses
- Net Balance
- Monthly Spending
- Spending by Category
- Largest Expense
- Transaction Count
- Remaining Budget

---

## FR7 Search

Users shall be able to search transactions by:

- Category
- Date
- Amount
- Description

---

## FR8 Data Storage

The application shall:

- Automatically save changes
- Automatically load saved data
- Preserve data between sessions

---

# 4. Non-Functional Requirements

## Performance

The system shall:

- Start within 3 seconds.
- Save records in less than 1 second.
- Handle at least 10,000 transactions efficiently.

---

## Reliability

The application shall:

- Prevent data corruption.
- Validate user inputs.
- Recover gracefully from unexpected errors.

---

## Security

The application shall:

- Reject invalid numeric inputs.
- Reject invalid dates.
- Prevent negative financial amounts.
- Protect stored data from accidental overwrite during normal operation.

---

## Usability

The application shall provide:

- Clear navigation menus.
- User-friendly prompts.
- Helpful error messages.
- Consistent interface design.

---

## Maintainability

The project shall use a modular architecture with separate folders for:

- Models
- Services
- Storage
- Utilities

---

## Portability

The application shall run on:

- Ubuntu
- Windows
- macOS

without requiring modifications.

---

# 5. System Architecture

```text
                    +----------------+
                    |    main.py     |
                    +-------+--------+
                            |
                            v
                 +----------------------+
                 |      CLI Menu        |
                 +----------+-----------+
                            |
        +-------------------+-------------------+
        |                   |                   |
        v                   v                   v
+----------------+  +----------------+  +----------------+
| Income Service |  | Expense Service|  | Budget Service |
+--------+-------+  +--------+-------+  +--------+-------+
         |                   |                   |
         +---------+---------+---------+---------+
                   |                   |
                   v                   v
             +-------------------------------+
             |         Data Manager          |
             +---------------+---------------+
                             |
                             v
                  +-------------------------+
                  |       JSON Storage      |
                  +-------------------------+
```

---

# 6. Data Storage

Project Structure

```text
smartspend/
│
├── data/
│   ├── profile.json
│   ├── income.json
│   ├── expenses.json
│   └── budget.json
│
├── models/
├── services/
├── storage/
├── utils/
└── main.py
```

---

# 7. Assumptions

The project assumes that:

- Python is installed.
- Users have permission to create and modify files.
- JSON files can be created automatically if missing.
- The application is used by one person.

---

# 8. Limitations

Version 1.0 does not support:

- Multiple users
- Cloud synchronization
- Online banking integration
- Database systems
- Mobile applications
- Graphical User Interface (GUI)
- Password authentication
- Data encryption

---

# 9. Future Enhancements

Future versions may include:

- SQLite integration
- MySQL integration
- Password-protected accounts
- User authentication
- CSV export
- PDF financial reports
- Charts and analytics
- Savings goals
- Recurring transactions
- Data backup and restore
- Desktop GUI (Tkinter or PyQt)
- Web version using Flask or Django

---

# Appendix A: Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Application Development |
| JSON | Data Storage |
| Git | Version Control |
| GitHub | Project Hosting |
| VS Code | Development Environment |

---

# Appendix B: Success Criteria

The project will be considered successful if users can:

- Create and manage a profile.
- Record income and expenses.
- Edit and delete transactions.
- Set monthly budgets.
- View financial reports.
- Search financial records.
- Save and reload data without loss.
- Operate the application entirely from the command line.

---

**End of Software Requirements Specification**
