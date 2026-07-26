# ------------------- ABC Bank Digital Portal ------------------- #
# ------------------- Contributor : Mohit singh & Dev Chauhan ------------------- #
# ------------------- Date : 25/07/2026 ------------------- #
# ------------------- Concepts involvement : File handling, Exception handling, String manipulation, Data entry and updation, Input validation, Basic If-else statements, Loops, Functions ------------------- #


from datetime import datetime

count = 0

# validating the date of birth format

def check_DOB(x):
    try:
        datetime.strptime(x, "%d %m %Y")
        return True
    except ValueError:
        return False


# Welcoming the user to the digital portal of ABC bank and providing options for different banking services

print("\n---------Welcome to Digital portal of ABC bank--------\n")
	
print("1) Create Account\n2) Withdraw / Deposit amount\n3) Check balance\n4) Get account details\n5) Transfer Money to other's Account\n6) Exit")
	

choose = int(input("\nChoose the serial number of your required Service :   "))
	
if choose == 1:
      name = input("\nEnter your full name : ")
      DOB = input("Enter your date of birth (dd mm yyyy) : ")
      adress = input("Enter your address : ")
      phone = input("Enter your 10 digit phone number : ")
      pin = input("Create your 4 digit PIN : ")

      for i in name:
            if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ":
                  print("\nInvalid name format. Please enter a valid name.")
                  exit()
            else:
                  if check_DOB(DOB) == False:
                        print("\nInvalid date of birth format. Please enter a valid date in the format dd mm yyyy.")
                        exit()
                  else:
                        if len(phone) != 10 or not phone.isdigit():
                              print("\nInvalid phone number format. Please enter a valid 10 digit phone number.")
                              exit()
                        else:
                              if len(pin) != 4 or not pin.isdigit():
                                    print("\nInvalid PIN format. Please create a 4 digit PIN.")
                                    exit()
                              else:
                                    with open("new.txt", "r") as f:
                                          lines = f.read().splitlines()
                                          for i in range(len(lines)):
                                                
                                                if lines[i].startswith("Account Number :"):
                                                      count += 1

                                    with open("new.txt","a") as f:
                                          f.write(f"Account Number : 1000000{count+1}\n\nName : {name}\nDOB : {DOB}\nBalance(₹) : 0\nUnique code : X8Y9{count + 1}\nPhone Number : {phone}\nAddress : {adress}\nPIN : {pin}\n\n\n")

                                    print(f"\nChecking credentials...\n\nChecking name format...\nChecking date of birth format...\nChecking phone number format...\nChecking PIN format...\n\nAll credentials are valid.\n\nCreating your account...\n\nAccount created successfully!\n\nYour account number is : 1000000{count+1}\n\nPlease keep your account number and unique code safe for future reference. Thank you!\n")

                                    break

elif choose == 6:
      print("\nThank you for using our services. Have a great day!\n")
      exit()

#creating deposit and withdraw feature

elif choose == 2:
      unique_code = input("\nEnter your unique code : ") #TAKING UNIQUE CODE
      with open("new.txt", "r") as f:
            read = f.read().splitlines()

            for i in range(len(read)):
                  if read[i] == f"Unique code : {unique_code}":  #checking availability of unique code in the file

                        try:
                              code = int(input("\nEnter your 4 digit PIN : ")) #taking PIN

                        except ValueError:
                              print("\nInvalid input. Please enter a valid 4 digit PIN.\n")
                              exit()

                        if code == int(read[i+3].split(" ")[2]): #checking PIN 

                              #ASKING FOR DEPOSIT OR WITHDRAWAL

                              print("\n1) Deposit\n2) Withdraw")
                              choice = int(input("\nChoose an option : "))

                              if choice == 1:
                                    try:
                                          deposit_amount = int(input("\nEnter the amount to deposit : "))
                                          if deposit_amount >= 0:
                                                balance = int(read[i-1].split(" ")[2]) + deposit_amount

                                                read[i-1] = f"Balance(₹) : {balance}"

                                                with open("new.txt", "w") as f:
                                                      f.write("\n".join(read))

                                                print("Checking unique code...\nChecking PIN...\n\nCredentials verified.\n\nProcessing your deposit...\n\nDeposit successful!\n")

                                                print(f"\nDeposit successful! Your new balance is: {balance}\n")
                                                break

                                          else:
                                                print("\nInvalid deposit amount. Please enter a positive value.\n")
                                                exit()

                                    except ValueError:
                                          print("\nInvalid input. Please enter a valid amount.\n")
                                          exit()
                              elif choice == 2:
                                    try:
                                          withdraw_amount = int(input("\nEnter the amount to withdraw : "))

                                          if withdraw_amount <= int(read[i-1].split(" ")[2]):

                                                balance = int(read[i-1].split(" ")[2]) - withdraw_amount
                                                read[i-1] = f"Balance(₹) : {balance}"
                                                with open("new.txt","w") as f:
                                                      f.write("\n".join(read))

                                                print("Checking unique code...\nChecking PIN...\n\nCredentials verified.\n\nProcessing your withdrawal...\n\nWithdrawal successful!\n")

                                                print(f"\nWithdrawal successful! Your new balance is: {balance}\n")

                                                break

                                          else:
                                                print("\nInsufficient balance. Please enter a valid amount.\n")
                                                exit()
                                    except ValueError:
                                          print("\nInvalid input. Please enter a valid amount.\n")
                                          exit()

                              else:
                                    print("\nInvalid choice. Please select a valid option.\n")
                        else:
                              print("\nInvalid PIN. Please enter the correct PIN.\n")
                              exit()
                  else:
                        if i == len(read) - 1:
                              print("\nInvalid unique code, No account found. Please enter a valid unique code.\n")
                              exit()
                        else:
                              continue

elif choose == 4:   
      unique_code = input("\nEnter your unique code : ") #TAKING UNIQUE CODE

      with open("new.txt" , 'r') as f:
            read = f.read().splitlines()

            for i in range(len(read)):
                  if read[i] == f"Unique code : {unique_code}":

                        try:
                              code = int(input("\nEnter your 4 digit PIN : ")) #taking PIN

                              if code == int(read[i+3].split(" ")[2]): #checking PIN
                                    print("\nChecking unique code...\nChecking PIN...\n\nCredentials verified.\n\nFetching your account details...\n")

                                    print(f"{read[i-4]}\n{read[i-3]}\n{read[i-2]}\n{read[i-1]}\n{read[i]}\n{read[i+1]}\n{read[i+2]}\n{read[i+3]}\n")

                                    break
                              else:
                                    print("\nInvalid PIN. Please enter the correct PIN.\n")
                                    exit()
                        except ValueError:
                              print("\nInvalid input. Please enter a valid 4 digit PIN.\n")
                              exit()
                  else:
                        if i == len(read) - 1:
                              print("\nInvalid unique code, No account found. Please enter a valid unique code.\n")
                              exit()
                        else:
                              continue

# CReating a feature to check the account balance

elif choose == 3:
      unique_code = input("\nEnter your unique code : ") #TAKING UNIQUE CODE
      with open("new.txt" , 'r') as f:
            read = f.read().splitlines()

            for i in range(len(read)):
                  if read[i] == f"Unique code : {unique_code}":
                        try:
                              code = int(input("\nEnter your 4 digit PIN : ")) #taking PIN

                              if code == int(read[i+3].split(" ")[2]): #checking PIN

                                    print("\nChecking unique code...\nChecking PIN...\n\nCredentials verified.\n\nFetching your account balance...\n")

                                    print(f"\nYour current balance is: ₹{read[i-1].split(' ')[2]}\n")

                                    break
                              else:
                                    print("\nInvalid PIN. Please enter the correct PIN.\n")
                                    exit()
                        except ValueError:
                              print("\nInvalid input. Please enter a valid 4 digit PIN.\n")
                              exit()
                  else:
                        if i == len(read) - 1:
                              print("\nInvalid unique code, No account found. Please enter a valid unique code.\n")
                              exit()
                        else:
                              continue

elif choose == 5:
      unique_code = input("\nEnter your unique code : ") #TAKING UNIQUE CODE
      with open("new.txt" , 'r') as f:
            read = f.read().splitlines()

            for i in range(len(read)):
                  if read[i] == f"Unique code : {unique_code}":
                        try:
                              code = int(input("\nEnter your 4 digit PIN : ")) #taking PIN

                              if code == int(read[i+3].split(" ")[2]): #checking PIN

                                    print("\nChecking unique code...\nChecking PIN...\n\nCredentials verified.\n\nFetching your account details...\n")
								  
                                    sender_balance = int(read[i-1].split(' ')[2])

                                    receiver_account_number = input("\nEnter the receiver's account number : ")
                                    transfer_amount = int(input("\nEnter the amount to transfer : "))

                                    if transfer_amount <= sender_balance:

                                          #checking if the receiver's account number exists in the file

                                          for j in range(len(read)):
                                                if read[j] == f"Account Number : {receiver_account_number}":

                                                      receiver_balance = int(read[j+3].split(' ')[2])
                                                      receiver_balance += transfer_amount
                                                      read[j+3] = f"Balance(₹) : {receiver_balance}"
                                                      read[i-1] = f"Balance(₹) : {sender_balance - transfer_amount}"

                                                      with open("new.txt", "w") as f:
                                                            f.write("\n".join(read)) #updating both sender's and reciever's balance

                                                      print("\nChecking unique code...\nChecking PIN...\n\nCredentials verified.\n\nProcessing your transfer...\n\nTransfer successful!\n")


                                                      break
                                                else:
                                                      if j == len(read) - 1:
                                                            print("\nInvalid receiver's account number. Please enter a valid account number.\n")
                                                            exit()
                                                      else:
                                                            continue
                                    else:
                                          print("\nInsufficient balance. Please enter a valid amount.\n")
                                          exit()
                              else:
                                    print("\nInvalid PIN. Please enter the correct PIN.\n")
                                    exit()

                        except ValueError:
                              print("\nInvalid input. Please enter a valid 4 digit PIN.\n")
                  else:
                        if i == len(read) - 1:
                              print("\nInvalid unique code, No account found. Please enter a valid unique code.\n")
                              exit()
                        else:
                              continue

else:
      print("\nInvalid choice. Please select a valid option.\n")
      exit()
