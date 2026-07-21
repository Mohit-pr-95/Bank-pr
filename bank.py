class Accounts:
	def __init__(self,name,DOB,an,PIN,balance,code):
		self.name = name
		self.DOB = DOB
		self.an = an
		self.PIN = PIN
		self.balance = balance
		self.code = code
		
	def info(self):
		print(f"Account created Successfully - \n\n• Account Number : {self.an}\n• Name : {self.name}\n• DOB : {self.DOB}\n• Balance : {self.balance}\n• Unique code : {self.code}\n")
		
count = 0

print("\n---------Welcome to Digital portal of ABC bank--------\n")
	
print("1) Create Account\n2) Withdraw amount\n3) Check balance\n4) Get account details\n5) Transfer Money to other's Account\n6) Exit")
	

choose = int(input("\nChoose the serial number of your required Service :   "))
	
if choose == 1:
	for i in range(1,4):
		print("\nEnter below asked Details\n")
		name = input("• Enter Your name :   ")
		DOB = input("\n• Enter Your DOB as DD MM YYYY :   ")
		
		adhar = int(input("\n• Enter your Adhar number :   "))
		pin = int(input("\n• Create a 4-Digit PIN for your account :   "))
		phone = int(input("\n• Enter your Phone number :   "))
		
		if len(DOB.strip()) == 10 and len(str(adhar)) == 12 and len(str(pin)) == 4 and len(str(phone)) == 10:
			
			with open("new.txt","r") as f:
				read = f.read().splitlines()
				
			for i in range(len(read)):
				if read[i][::-1].endswith("cA"):
					count += 1
					
				else:
					continue
			
			ac1 = Accounts(name = name , DOB = DOB , PIN = pin , balance = 0 , an = f"M12S959{count+1}", code = f"X8Y90{count+1}")
			
			with open("new.txt", "a") as f:
				f.write(f"Account {count+1} - \n")
				f.write(f"• Name : {ac1.name}\n")
				f.write(f"• DOB : {ac1.DOB}\n")
				f.write(f"• Account number : {ac1.an}\n")
				f.write(f"• PIN : {ac1.PIN}\n")
				f.write(f"• Balance : {ac1.balance}\n")
				f.write(f"• Unique account code : {ac1.code}\n\n")
			
			print("\nChecking Credentials.....Done\nChecking uniqueness of PIN.....Done\nVerifying Phone mumber.....Done\n\nCreating account....")
			
			ac1.info()
			
			break
		else:
			if i == 3:
				print("Maximum request per session reached  ! , Restart the program..\n")
			else:
				print(f"Invalid Credentials, Try again ({3-i} attemps left)")
		
elif choose == 4:
	fetch = input("Enter your Account unique id : ")
	with open("new.txt","r") as p:
		lines = p.read().splitlines()
	
	for i in range(len(lines)):
		if lines[i] == f"• Unique account code : {fetch}":
			secretCode = int(input("Enter your PIN to get details : "))
			if lines[i-2] == f"• PIN : {secretCode}":
				print(f"\n{lines[i-5]}")
				print(f"\n{lines[i-4]}")
				print(f"\n{lines[i-3]}")
				print(f"\n{lines[i-1]}")
				print(f"\n{lines[i]}\n")
			else:
				print("Wrong PIN !!! ")
				
		else:
			continue
			
elif choose == 6:
	print("Thanks for visiting ABC Bank !!...")