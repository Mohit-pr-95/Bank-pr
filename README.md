# ABC Bank — Digital Portal (CLI)

A command-line banking prototype written in Python. Users are prompted through a menu to create an account or look up account details. Data is persisted in a local text file (`new.txt`) rather than a database.

## What actually works

| Menu option | Status |
|---|---|
| 1. Create Account | Implemented |
| 2. Withdraw amount | Listed  in menu  , Will be added soon
| 3. Check balance |  Listed in menu,  Will be added soon|
| 4. Get account details |  Implemented |
| 5. Transfer Money |  Listed in menu,  Will be added soon |
| 6. Exit | implemented |

## How it works

**Create Account (`1`)**
- Collects name, DOB, Aadhar number, 4-digit PIN, and phone number.
- Validates only the *length* of each field (DOB = 10 chars, Aadhar = 12 digits, PIN = 4 digits, phone = 10 digits) — not the actual format or content.(But will be done soon)
- Gives 3 attempts per session before locking out.
- Generates an account number and "unique code" by counting existing entries in `new.txt` (via a reversed-string check for lines starting with `"Ac"`), then appends the new record to that file in plain text.

**Get Account Details (`4`)**
- Asks for the account's unique code, scans `new.txt` for a matching line, then asks for the PIN.
- If the PIN matches, prints the account block by indexing fixed line offsets (`-5, -4, -3, -1, 0`) relative to the matched line.

## Data storage format (`new.txt`)

```
Account 1 - 
• Name : John Doe
• DOB : 01 01 2000
• Account number : M12S9591
• PIN : 1234
• Balance : 0
• Unique account code : X8Y901

```

## Requirements

- Python 3
- No external dependencies

## Running it

```bash
python bank.py
```

`new.txt` is created automatically the first time an account is created **if it already exists** — see Known Issues below.

## Known issues

- **First run crashes.** Account creation opens `new.txt` in read mode before it's ever been created, so choosing option `1` on a fresh setup throws `FileNotFoundError`. The file needs to exist (even empty) beforehand.
- **PINs, Aadhar numbers, and phone numbers are stored in plain text** with no hashing or encryption.
- **Leading zeros are silently dropped.** PIN, Aadhar, and phone are cast to `int`, so a PIN like `0123` becomes `123` and fails length validation.(Will be fixed soon)
- **No `try/except` around input parsing.** Entering non-numeric text for Aadhar/PIN/phone crashes the program.
- **Account lookup is position-dependent**, not key-based — it assumes every record is written in the exact same 6-line order forever. Any change to the write format breaks all existing lookups.
- **Menu advertises three features (withdraw, balance check, transfer) that don't exist yet.**
- **No amount/balance logic at all** — `balance` is hardcoded to `0` at creation and never updated anywhere.

#**All These things will be fixed in next Commit and new features will also be added , (about 2-3 days later)