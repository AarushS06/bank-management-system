# 🏦 DFDC Bank Management System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MySQL-Database-orange?logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
</p>

<p align="center">
  A command-line bank management system built with <b>Python</b> and <b>MySQL</b> — manage customer accounts, transactions, loans, and fixed deposits, all from your terminal.
</p>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Database Schema](#-database-schema)
- [Project Structure](#-project-structure)
- [Security Notes](#-security-notes)
- [Future Improvements](#-future-improvements)
- [License](#-license)
- [Author](#-author)

---

## 🔎 Overview

**Bank Management System** is a menu-driven CLI application that simulates core banking operations. It's designed as a practical, hands-on project to demonstrate database integration, CRUD operations, and real-world application logic using Python and MySQL.

---

## ✨ Features

- 🧾 **Customer Registration & Sign-In** — create a new account or securely log into an existing one
- ✏️ **Profile Management** — view and update account details (name, DOB, mobile number, Aadhaar, password)
- 💸 **Transactions** — deposit and withdraw funds with full transaction history tracking
- 🏦 **Loans** — apply for loans and track repayment details
- 📈 **Fixed Deposits (FD)** — open FDs and calculate maturity amounts automatically

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Database | MySQL |
| DB Connector | PyMySQL |
| Interface | Command-Line (CLI) |

---

## 📋 Requirements

- Python 3.x
- MySQL Server (running locally)
- `pymysql` library

Install dependencies:

```bash
pip install pymysql
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/bank-management-system.git
   cd bank-management-system
   ```

2. **Set up MySQL**
   Make sure MySQL Server is installed and running locally.

3. **Set your database password as an environment variable**
   For security, the script reads your MySQL password from an environment variable instead of storing it in code.

   | OS | Command |
   |---|---|
   | Windows (CMD) | `set DB_PASSWORD=your_password_here` |
   | Windows (PowerShell) | `$env:DB_PASSWORD="your_password_here"` |
   | macOS/Linux | `export DB_PASSWORD=your_password_here` |

4. **Run the application**
   ```bash
   python bank_management.py
   ```

   The database and required tables are created automatically on first run.

---

## 🚀 Usage

On launch, you'll see a main menu:

```
1. Sign In
2. Registration
3. Exit the program
```

- **New users** → choose **Registration**, fill in your details, and receive an auto-generated account number.
- **Existing users** → choose **Sign In** to access your account, view your balance, make transactions, apply for a loan, or open a fixed deposit.

---

## 🗄 Database Schema

The system automatically creates a database called `bank_management` with the following tables:

| Table | Purpose |
|---|---|
| `customer` | Stores customer profile info (name, DOB, Aadhaar, balance, mobile, password) |
| `transaction` | Logs every deposit/withdrawal with date, time, and mode |
| `loan` | Tracks issued loans, interest rate, tenure, and repayment |
| `fd` | Tracks fixed deposits, maturity date, and maturity amount |

---

## 📁 Project Structure

```
bank-management-system/
├── bank_management.py   # Main application script
└── README.md             # Project documentation
```

---

## 🔐 Security Notes

- Database credentials are **never hardcoded** — they're loaded from the `DB_PASSWORD` environment variable.
- This project is for **educational purposes** and isn't hardened for production use (e.g. passwords are stored in plain text in the database, not hashed).

---

## 🔮 Future Improvements

- [ ] Hash passwords instead of storing them in plain text
- [ ] Add input validation for all fields
- [ ] Move hardcoded interest rates into a config file
- [ ] Add unit tests
- [ ] Build a GUI or web front-end

---

## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 👤 Author

**Aarush**

If you found this project useful, consider giving it a ⭐ on GitHub!
