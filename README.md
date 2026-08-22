# smart-Spend 💰

> **Take control of your money. One transaction at a time.**

**smart-Spend v1.0.0** is a personal finance management application that helps users track income, manage expenses, create budgets, monitor their financial activity, and understand their spending habits.

Built with Python, smart-Spend provides a simple and structured way to manage everyday finances without requiring any programming knowledge.

---

## ✨ Features

### 👤 Profile Management

Create and manage your personal financial profile.

* Name
* Email
* Preferred currency
* Profile information

### 💰 Income Management

Record and manage money coming into your finances.

Examples include:

* Salary
* Freelance income
* Business income
* Gifts
* Other income sources

### 💸 Expense Management

Record and organize everyday spending.

Expenses can be categorized into areas such as:

* Food
* Transport
* Housing
* Bills
* Entertainment
* Education
* Healthcare
* Other

### 🎯 Budget Management

Set spending limits and monitor your progress against them.

Budgets help answer:

> **"How much can I still spend?"**

### 🔎 Search

Find financial records quickly instead of manually going through every transaction.

### 📊 Financial Reports

smart-Spend provides useful financial summaries including:

* Total income
* Total expenses
* Number of incomes
* Number of expenses
* Highest income
* Highest expense
* Current balance
* Savings rate

### 💾 Persistent Storage

Your financial records are stored locally so that your information remains available between application sessions.

### ✅ Input Validation

User input is validated before being processed to prevent invalid financial records and reduce application errors.

### 🧪 Automated Testing

The project includes tests for core functionality to help maintain reliability as the application evolves.

---

# 🖥️ User Experience

smart-Spend is designed for people who may have **zero programming knowledge**.

The application provides a guided menu-driven interface:

```text
══════════════════════════════════════
             smart-Spend
══════════════════════════════════════

1. Income
2. Expenses
3. Budgets
4. Reports
5. Search
6. Profile
0. Exit

Choose an option:
```

Users interact with the application through simple choices and prompts rather than needing to interact with the underlying files or code.

---

# 🏗️ Architecture

smart-Spend uses a layered structure that separates the application's responsibilities.

```text
                    smart-Spend
                         │
                         ▼
                ┌─────────────────┐
                │   User Interface │
                │      / CLI       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Handlers      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Services      │
                │  Business Logic  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │     Storage      │
                │   Persistence    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │      JSON        │
                │      Data        │
                └─────────────────┘
```

This architecture keeps user interaction, business logic, data models, and persistence separate.

As a result, the application can be maintained and extended without placing the entire system inside a single file.

---

# 📁 Project Structure

```text
smart-Spend/
│
├── assets/
│   └── CLI assets and application resources
│
├── data/
│   └── Local application data
│
├── docs/
│   └── Project documentation
│
├── handlers/
│   └── User interaction and feature handlers
│
├── models/
│   └── Application data models
│
├── services/
│   └── Core business logic
│
├── storage/
│   └── Data persistence functionality
│
├── tests/
│   └── Automated tests
│
├── utils/
│   └── Shared utilities and helpers
│
├── main.py
│   └── Application entry point
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
    └── Project documentation
```

---

# 🛠️ Technology Stack

| Technology | Purpose                 |
| ---------- | ----------------------- |
| **Python** | Application development |
| **JSON**   | Local data persistence  |
| **Pytest** | Automated testing       |
| **Git**    | Version control         |
| **GitHub** | Source code hosting     |

---

# 🚀 Installation

## Prerequisites

Make sure you have:

* Python 3.x
* Git
* A terminal

Verify Python:

```bash
python3 --version
```

Verify Git:

```bash
git --version
```

---

## 1. Clone the repository

```bash
git clone https://github.com/jlmushumba/smart-Spend.git
```

## 2. Enter the project directory

```bash
cd smart-Spend
```

## 3. Create a virtual environment

```bash
python3 -m venv .venv
```

## 4. Activate the virtual environment

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running smart-Spend

Start the application with:

```bash
python3 main.py
```

The smart-Spend main menu will appear in your terminal.

Follow the prompts to:

1. Create your profile
2. Add income
3. Add expenses
4. Create budgets
5. Search transactions
6. View reports
7. Manage your profile

---

# 🧪 Testing

Run the complete test suite:

```bash
pytest
```

For detailed test output:

```bash
pytest -v
```

A reliable financial application needs predictable behavior, so testing is part of the development workflow rather than an afterthought.

---

# 📊 Financial Calculations

smart-Spend uses straightforward financial calculations to provide useful information.

### Balance

```text
Balance = Total Income - Total Expenses
```

### Savings Rate

```text
Savings Rate =
(Total Income - Total Expenses)
÷ Total Income × 100
```

These calculations allow users to understand their overall financial position and spending behavior.

---

# 💾 Data Storage

Version 1.0.0 uses **JSON-based local storage**.

Application data is separated into dedicated files rather than being stored directly inside the Python source code.

This approach keeps the first version lightweight and easy to run without requiring users to install and configure a database server.

---

# 🔒 Data & Privacy

In v1.0.0, financial data is stored locally on the user's machine.

smart-Spend does not require a cloud account or external financial service to operate.

This means the application can be used without sending personal financial records to a remote server.

> **Important:** v1.0.0 is a local application and should not be considered a production-grade financial platform for sensitive or regulated financial data.

---

# 🌍 Global Vision

Version 1.0.0 establishes the foundation for a larger vision.

The long-term goal of smart-Spend is to become a **global personal finance platform** that can adapt to users from different countries and financial environments.

Future versions may introduce:

* 🌎 Multi-country support
* 💱 Multiple currencies
* 🌐 Multiple languages
* 📱 Mobile-friendly interfaces
* 🖥️ Web application
* 📊 Advanced financial analytics
* 🎯 Financial goals
* 🔁 Recurring transactions
* ☁️ Secure cloud synchronization
* 📈 Advanced reporting
* 🔐 User authentication
* 🗄️ Production database
* 🔗 Financial service integrations where appropriate

The global vision is:

> **Personal finance management that is simple enough for everyone, regardless of where they live or how much they know about technology.**

---

# 🗺️ Version History

## v1.0.0 — Initial Release

The first complete release of smart-Spend.

### Included

* User profile management
* Income management
* Expense management
* Budget management
* Financial reports
* Transaction search
* Input validation
* JSON persistence
* CLI navigation
* Automated testing
* Modular application architecture
* Project documentation

**Release status:** `Stable`

---

# 📌 Project Status

**Current Version: `v1.0.0`**

smart-Spend v1.0.0 is the first stable release of the application.

The project began as a Python CLI application focused on building a solid financial management foundation.

Future development will focus on turning that foundation into a more accessible application for everyday users, including a web-based interface and broader international support.

---

# 🤝 Contributing

Contributions and feedback are welcome.

If you discover a bug, have a feature suggestion, or want to improve the project:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Add or update tests where appropriate.
5. Commit your changes.
6. Open a pull request.

For bugs and feature requests, GitHub Issues can be used to document the problem or proposal.

---

# 👨‍💻 Author

**Jean Louange MUSHUMBA**

Developer and creator of smart-Spend.

---

# ⭐ Support

If you find the project useful or interesting, consider giving the repository a ⭐ on GitHub.

Feedback, suggestions, and ideas are always welcome.

---

# 📄 License

See the repository license file for the terms governing the use and distribution of smart-Spend.

---

<div align="center">

**smart-Spend v1.0.0**

*Understand your money. Control your spending. Build your future.*

</div>
