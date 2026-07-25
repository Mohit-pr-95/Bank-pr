# ABC Bank — Digital Portal (CLI)

A command-line banking system written in Python. Users interact through a text menu to create an account, manage funds, and view account details. All data is stored locally in a plain-text file (`new.txt`) — no database or external dependencies required.

## Features

| # | Feature | Status |
|---|---|---|
| 1 | Create Account |  Implemented |
| 2 | Deposit / Withdraw |  Implemented |
| 3 | Check Balance |  Implemented |
| 4 | Get Account Details |  Implemented |
| 5 | Transfer Money |  Implemented |
| 6 | Exit | Implemented |

## How it works

**Create Account**
Collects name, date of birth, address, phone number, and a 4-digit PIN. Validates that the name contains only letters/spaces, the DOB matches `dd mm yyyy`, the phone number is exactly 10 digits, and the PIN is exactly 4 digits. On success, generates an account number and a unique code, then appends the record to `new.txt`.

**Deposit / Withdraw, Check Balance, Get Details, Transfer**
Each of these asks for your unique code and PIN, verifies them against `new.txt`, then reads or updates your balance in place. Transfers also verify that the receiver's account number exists before moving funds.

## Requirements

- Python 3
- No external dependencies (standard library only)

## Running it

```bash
python bank.py
```

`new.txt` must exist in the same directory (it can be empty) before you create your first account — it's included in this repo already set up.

## Data storage format (`new.txt`)

Each account is stored as a plain-text block:

```
Account Number : 10000001

Name : John Doe
DOB : 01 01 2000
Balance(₹) : 0
Unique code : X8Y91
Phone Number : 9876543210
Address : 123 Main Street
PIN : 1234

```

## Known limitations

- **No encryption.** PINs, phone numbers, and addresses are stored in plain text. This is a learning project, not a production-ready system.
- **Position-dependent lookups.** Records are read by counting fixed line offsets from a matched line, so every account must follow the exact same format — a stray blank line or reordered field will break lookups.
- **Limited input safety.** Menu selection and money amounts aren't wrapped in error handling, so non-numeric input will crash the program.

## Concepts practiced

File handling, exception handling, string manipulation, data entry and updates, input validation, conditionals, loops, and functions.

## Contributors

Mohit Singh & Dev Chauhan
