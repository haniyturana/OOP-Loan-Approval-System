# 💳 OOP Loan Approval System

An interactive banking tool built in Python to evaluate loan eligibility using **Object-Oriented Programming (OOP)**. This system automates financial risk assessment by analyzing Debt-to-Income (DTI) ratios and Credit Scores.

---

## 🏗️ Project Architecture (The "Steps")
This project is structured into four distinct parts to demonstrate the evolution of software development from simple scripts to a full OOP system:

* **Part 1: Functional Foundation** (`step1_Pt3_definefunction.ipynb`)
    * The starting point of the project. Here, I built the basic banking logic using standard functional programming (`def` functions) before refactoring into an OOP structure.
* **Part 2: The Core Logic** (`step2_Pt2_module.py`)
    * The "Brain" of the system. This Python module contains the `Customer` (Parent) and `CreditScoreCustomer` (Child) classes, implementing core concepts like **Inheritance** and **Encapsulation**.
* **Part 3: Unit Testing** (`step3_Pt3_creditfunction_test.ipynb`)
    * A dedicated testing environment to ensure every method and calculation within the module is accurate before being deployed to the end-user.
* **Part 4: Interactive Interface** (`step4_loan_test.ipynb`)
    * The final product. A complete Command Line Interface (CLI) that allows users to input data interactively and receive real-time loan approval decisions.

---

## 🌟 Key Features
* **Interactive CLI**: User-friendly interface with a data verification layer (`Proceed y/n`) to ensure accuracy.
* **Automated Risk Scoring**: Automatically categorizes applicants as *Low, Medium,* or *High Risk*.
* **Compensating Factor Logic**: A "smart" policy where an excellent DTI ratio can override a mediocre credit score for approval.
* **Robust Error Handling**: Implements `try-except` blocks to prevent system crashes during invalid data entry.

---

## 🧠 OOP Concepts Applied
This project serves as a deep dive into the fundamental pillars of Object-Oriented Programming:

1. **Inheritance**: Utilizing a base `Customer` class and extending it into a specialized `CreditScoreCustomer` class.

2. **Encapsulation**: Bundling financial data and evaluation logic within classes to ensure data integrity and organized code.

3. **Abstraction**: Hiding complex banking risk policies behind simple, reusable method calls like `.evaluate_loan()`.

---

## 🚀 How to Run
1. Clone this repository.
2. Ensure `step2_Pt2_module.py` is in the same directory as the Notebooks.
3. Open and run `step4_loan_test.ipynb` to start the interactive application.

---

*This project was developed as a practical exercise in Python OOP and Banking Logic.*
