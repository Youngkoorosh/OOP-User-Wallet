# Python User Wallet System

This is a simple Python command-line application that simulates a basic user wallet system. It allows users to register, deposit funds, and withdraw funds (with a transaction fee).

## Features

* **User Registration**: Create new user accounts with an initial balance.
* **Fund Deposit**: Add money to an existing user's account.
* **Balance Check/Withdrawal**: Retrieve a user's balance and deduct a fixed fee ($10) for the transaction.

## How to Run

1.  **Save the Code**: Save the provided Python code into a file named `main.py` (or any other `.py` extension).

2.  **Run from Terminal**: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script using:

    ```bash
    python main.py
    ```

3.  **Input Commands**: The program will then prompt you to enter the number of operations (`n`), followed by `n` lines of commands.

## Commands

The system accepts the following commands:

* **`REGISTER <username> <timestamp>`**
    * Registers a new user.
    * Example: `REGISTER Alice 1678886400`
    * Returns: "Registered Successfully" or "Duplicate User!"

* **`DEPOSIT <username> <amount> <timestamp>`**
    * Deposits a specified `amount` into the user's account.
    * Example: `DEPOSIT Alice 50 1678886500`
    * Returns: The new balance or "No Such User Found!"

* **`GET_BALANCE <username> <timestamp>`**
    * Retrieves the user's balance. A $10 fee is deducted for this operation.
    * Example: `GET_BALANCE Alice 1678886600`
    * Returns: The new balance after deduction, "No Such User Found!", or "Not Enough Fund!"

## Example Usage

Here's an example of how you might interact with the program:

**Input:**
```bash
5
REGISTER Alice 1678886400
DEPOSIT Alice 50 1678886500
GET_BALANCE Alice 1678886600
REGISTER Bob 1678886700
GET_BALANCE Bob 1678886800
```
**Output:**
```bash
Registered Successfully
150
140
Registered Successfully
90
```
## Code Structure and OOP Principles

* **`User` Class**: This class encapsulates the data (name, money) and behavior related to a single user. Each `User` object is an instance of this class, demonstrating **encapsulation** and **data abstraction**.
* **`users` List**: A global list that stores instances of the `User` class. While simple, in a larger application, this would typically be managed by another class or a database layer.
* **Functions (`register`, `deposit`, `get_balance`)**: These functions interact with the `User` objects, showcasing how methods would be used to manipulate object states in a more complex OOP design. Although they are currently global functions operating on a global list, they effectively interact with the `User` objects, laying a foundation for further OOP refinement (e.g., creating a `WalletManager` class).

## Limitations

* **No Persistence**: User data is not saved and will be lost when the program closes.
* **Simple Error Handling**: Error messages are basic.
* **Fixed Fee**: The `GET_BALANCE` operation always deducts a fixed $10.
* **Timestamp Unused**: The `timestamp` argument is currently not utilized in any of the functions for logic, but it's passed through. This could be extended for logging or transaction history.
