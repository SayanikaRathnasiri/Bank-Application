
total_balance=10000.0

#Balance Checking
def check_account_balance():
    global total_balance
    #Annual Interest Rate = 5%
    interest=total_balance*(5/100)*(1/12)
    total_balance+=interest
    
#--------------------------------------------------------------------------------------------------------------------
#Cash Deposite
def cash_deposit(dep_amount):
    global total_balance
    
    if dep_amount>0:
        total_balance+=dep_amount
        check_account_balance()
        return '*** Deposit Successful ! ***'
    else:
        return '*** Deposit was not Successful ! ***'

#--------------------------------------------------------------------------------------------------------------------
#Cash Withdrawal
def cash_withdrawal(withdrawal_amount):
    global total_balance
     
    if withdrawal_amount<total_balance:
        total_balance-=withdrawal_amount
        return '*** Withdrawal Successful ! ***'
    else:
        return '*** Withdrawal was not Successful ! ***'

#--------------------------------------------------------------------------------------------------------------------       
#Get a loan
def get_loan(year,loan_amount):
    
    month = year*12
    if year==3:
        rate=0.15
        Monthly_payment=(rate/12)*(1/(1-(1+rate/12)**(-month)))*loan_amount
        print("Monthly Payment : ",Monthly_payment)
        return '*** The Monthly Payment Was Processed ***'
    elif year==5:
        rate=0.20
        Monthly_payment=(rate/12)*(1/(1-(1+rate/12)**(-month)))*loan_amount
        print("Monthly Payment : ",Monthly_payment)
        return '*** The Monthly Payment Was Processed ***'
    elif year==7:
        rate=0.25
        Monthly_payment=(rate/12)*(1/(1-(1+rate/12)**(-month)))*loan_amount
        print("Monthly Payment : ",Monthly_payment)
        return '*** The Monthly Payment Was Processed ***'
    elif year>7:
        rate=0.30
        Monthly_payment=(rate/12)*(1/(1-(1+rate/12)**(-month)))*loan_amount
        print("Monthly Payment : ",Monthly_payment)
        return '*** The Monthly Payment Was Processed ***'
    else:
        return '*** Sorry! Enter Currect Details ***'
    
#--------------------------------------------------------------------------------------------------------------------
#main_menu
def main_menu():
    print("\n-----WELCOME TO BANKING SYSTEM-----")
    print("\n1.Check Account Balance\n2.Cash Deposit\n3.Cash Withdrawal\n4.Get a Loan\n5.Exit")
    choice =int(input("\nEnter Your Choice (1) or (2) or (3) or (4) or (5): "))
    
    while(choice<=5):
        if choice == 1:
            check_account_balance()
            print("\n------------------------------------------------")
            print("---Showing Current Balance---")
            print("\nYour Current Balance : ",total_balance)
            print("------------------------------------------------\n")

            print("\n-----WELCOME TO BANKING SYSTEM-----")
            print("\n1.Check Account Balance\n2.Cash Deposit\n3.Cash Withdrawal\n4.Get a Loan\n5.Exit")
            choice =int(input("\nEnter Your Choice (1) or (2) or (3) or (4) or (5): "))

        elif choice == 2:
            print("\n------------------------------------------------")
            print("---Deposit of money---")
            dep_amount=float(input("\nEnter Your Deposite Amount : "))
            output=cash_deposit(dep_amount)
            print(output)
            #print("\nYour Current Balance : ",total_balance)
            print("------------------------------------------------\n")

            print("\n-----WELCOME TO BANKING SYSTEM-----")
            print("\n1.Check Account Balance\n2.Cash Deposit\n3.Cash Withdrawal\n4.Get a Loan\n5.Exit")
            choice =int(input("\nEnter Your Choice (1) or (2) or (3) or (4) or (5): "))

        elif choice == 3:
            print("\n------------------------------------------------")
            print("---Withdrawal of money---")
            withdrawal_amount=float(input("\nEnter Your Withdrawal Amount : "))
            output=cash_withdrawal(withdrawal_amount)
            print(output)
            #print("\nYour Current Balance : ",total_balance)
            print("------------------------------------------------\n")

            print("\n-----WELCOME TO BANKING SYSTEM-----")
            print("\n1.Check Account Balance\n2.Cash Deposit\n3.Cash Withdrawal\n4.Get a Loan\n5.Exit")
            choice =int(input("\nEnter Your Choice (1) or (2) or (3) or (4) or (5): "))

        elif choice == 4:
            print("\n------------------------------------------------")
            print("---Loan Details---\n")

            print("Years           Rate")
            print("3               15%")
            print("5               20%")
            print("7               25%")
            print("more than 7     30%")

            year=int(input("\nInput Years of loan :"))
            loan_amount=int(input("Input Amount of loan :"))
            output=get_loan(year,loan_amount)
            print(output)
            print("------------------------------------------------\n")
            print("\n-----WELCOME TO BANKING SYSTEM-----")
            print("\n1.Check Account Balance\n2.Cash Deposit\n3.Cash Withdrawal\n4.Get a Loan\n5.Exit")
            choice =int(input("\nEnter Your Choice (1) or (2) or (3) or (4) or (5): "))

        elif choice == 5:
            print("\n------------------------------------------------")
            print("--Thank You !--")
            print("------------------------------------------------\n")
            quit()
        else:
            print("*** Please Enter Valid Choise. ***")

#main_menu()