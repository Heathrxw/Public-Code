print("Welcome to the Trial Balance Calculator enter the values for each detail.")
print("If you dont have it put value as 0")
print("Debit Input")

Vehicles = input('Vehicles ')
Machinery = input('Machinery ')
Fixtures = input('Fixtures ')
Rent = input('Rent ')
Electricity = input('Electricity ')
Utilities = input('Utilities ')
Premises = input('Premises ')
OpeningInventory = input('Opening Inventory ')
Debtors = input('Debtors ')
Bank = input('Bank ')
Purchases = input('Purchases ')
Wages = input('Wages ')
RepairsAndRenewals = input('Repairs and Renewals ')
Rates = input('Rates ')
Insurance = input('Insurance ')
Sundry = input('Sundry ')
MotorExpenses = input('Motor Expenses ')
Drawings = input('Drawings ')
Marketing = input('Marketing ')
Advertising = input('Advertising ')
Equipment = input('Equipment ')
ReturnsIn = input('Returns In ')
CarriageOut = input('Carriage Out ')
CarriageIn = input('Carriage In ')

print("Credit Input")
Sales = input('Sales ')
BankOverdraft = input('Bank Overdraft ')
Creditors = input('Creditors ')
BankLoan = input('Bank Loan ')
Receivables = input('Receivables ')
CommissionReceived = input('Commision Received ')
DiscountsReceived = input('Discounts Received ')
Mortgage = input('Mortgage ')
ReturnsOut = input('Returns Out ')
RentReceived = input('Rent Received ')


Debit1 = int(Vehicles) + int(Machinery) + int(Fixtures) + int(Rent) + int(Electricity) + int(Utilities) + int(Premises) + int(OpeningInventory) + int(Debtors) + int(Bank) + int(Purchases) + int(Wages)
Debit2 = int(RepairsAndRenewals) + int(Rates) + int(Insurance) + int(Sundry) + int(MotorExpenses) + int(Drawings) + int(Marketing) + int(Advertising) + int(Debtors) + int(Bank) + int(Purchases)
Debit3 = int(Wages) + int(Equipment) + int(Equipment) + int(CarriageIn) + int(CarriageOut)
Credit = int(Sales) + int(BankOverdraft) + int(Creditors) + int(BankLoan) + int(Receivables) + int(CommissionReceived) + int(DiscountsReceived) + int(Mortgage) +int(ReturnsOut) +int(RentReceived)

DebitTotal=Debit1+Debit2+Debit3
#CreditTotal=Credit1+Credit2
print("The Debit Balance is: ",DebitTotal)
print("The Credit Balance is: ",Credit)
