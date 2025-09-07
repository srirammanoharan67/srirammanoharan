balance = 0
crr_pin = 2025

def Balance(balance):
    print(f"Current Balance : {balance}$")
    
def withdraw(balance,with_amt):
   if with_amt >= 100:
       if with_amt <= balance :
           balance =balance - with_amt
           print(f"{with_amt}$ is Debited from your account")
       else:
           print("Insufficient Amount For Withdrawal")
       
   else:
      print("Withdraw amount Greater than 99$")
      
   return balance
    
    
def deposit(balance,depo_amt):
    if depo_amt < 100:
        print("Deposit amount must greater than 100$")
    else:
        balance = balance + depo_amt
        print(f"{depo_amt}$ is Credited to your account")
    return balance
    
def Exit():
    print("Thanks For Visiting CUB")
    return False
   
def main(balance):
   is_true = True
   while is_true:
       #print("*************************Bank withdraw*************************")
       print()
       print("1.Balance")
       print("2.Withdraw")
       print("3.Deposit")
       print("4.Exit")
       choice =input("\nEnter your choice(1 to 4) : ")
       print("")
       if choice == '1' :
           Balance(balance)
           
       elif choice == '2' :
           with_amt = float(input("Enter Withdraw Amount : "))
           balance = withdraw(balance,with_amt)
           
       elif choice == '3' :
           depo_amt =float(input("Enter Deposit Amount : ")) 
           balance = deposit(balance,depo_amt)
           
       elif choice == '4':
           is_true = Exit()
           
       else:
           print(f"{choice} is not valid")
       print("")


count = 0
print("*************************Bank withdraw*************************\n")
while count < 3:
   atm_pin = int(input("Enter ATM Pin : "))
   if atm_pin == crr_pin:
      main(balance)
      break

   else:
      if count != 2:
         print("ATM Pin Is Wrong Enter Correct Pin")
      else:
         print("ATM Pin Is Wrong Enter Correct Pin\n")
         print("Your Account Is Blocked For 24 Hours")
   count = count + 1
   print()

          
        
        
