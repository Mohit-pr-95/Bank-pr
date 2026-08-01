# ABC Bank Digital Portal

A command-line banking system built in Python. It lets users create an account, deposit or withdraw money, check their balance, view account details, and transfer money to other account holders — all backed by a plain text file used as the account database.

**Contributors:** Mohit Singh, Dev Chauhan

## Features

| # | Option | Description |
|---|--------|-------------|
| 1 | Create Account | Register a new account with name, DOB, address, phone number, and a 4-digit PIN |
| 2 | Withdraw / Deposit | Add or remove funds from an existing account |
| 3 | Check Balance | View the current balance of an account |
| 4 | Get Account Details | View the full profile linked to an account |
| 5 | Transfer Money | Move funds from one account to another |
| 6 | Exit | Close the application |

## Requirements

- Python 3.x
- No external libraries — uses only the built-in `datetime` module

## Getting Started

1. Place `bank.py` and an empty `new.txt` file in the same folder. The program does not create `new.txt` automatically, so account creation will crash on a completely fresh setup without it (see Known Issues).
2. Run the program:
   ```bash
   python bank.py
   ```
3. Choose an option from the menu (1–6) and follow the prompts.

## How Accounts Are Identified

Every account gets two identifiers on creation:

- **Account Number** — sequential, format `1000000<n>` (e.g. `10000001`, `10000002`, …)
- **Unique Code** — sequential, format `X8Y9<n>` (e.g. `X8Y91`, `X8Y92`, …)

The **Unique Code + PIN** combination is required for deposits, withdrawals, balance checks, viewing details, and sending a transfer. The **Account Number** is used only as the destination when someone else sends you a transfer.

## Input Validation

| Field | Rule |
|-------|------|
| Name | Letters and spaces only |
| Date of Birth | Format `dd mm yyyy`, checked with `datetime.strptime` |
| Phone Number | Exactly 10 digits |
| PIN | Exactly 4 digits |

Any invalid entry stops the program immediately with an error message.

## Data Storage

Accounts are stored in `new.txt` as plain text, one block per account:

```
Account Number : 10000001

Name : John Doe
DOB : 15 08 2001
Balance(₹) : 5000
Unique code : X8Y91
Phone Number : 9876543210
Address : 123 Main Street
PIN : 1234

```

There's no encryption — PINs and personal details sit in the file as plain text, and every read/write operation relies on each field always being at a fixed line offset within the block.

## Known Issues / Limitations

- **Transfers don't credit the receiver.** The receiver's record is updated at the wrong line offset (their DOB line, not their Balance line), so the transferred amount never reaches their actual balance, and their DOB field gets overwritten with a balance string instead.
- **"Get Account Details" omits the account number.** An indexing offset prints a blank line where the `Account Number` field should be.
- **First run requires a pre-existing `new.txt`.** Account creation opens it in read mode before writing, so a missing file crashes with `FileNotFoundError` rather than being created automatically.
- **Withdrawals accept negative amounts.** Deposit checks for a non-negative value; withdrawal doesn't, so a negative withdrawal amount increases the balance instead of decreasing it.
- **An empty name exits silently.** Validation for DOB, phone, and PIN only runs inside the loop over the name's characters, so submitting an empty name skips all checks and ends the program with no account created and no error shown.

## License

Built for educational purposes.
