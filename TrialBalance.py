print("Welcome to the Trial Balance Calculator enter the values for each detail.")
print("Debit Input")
Debit1 = input('Vehicles ')
Debit2 = input('Machinery ')

print("Credit Input")
Credit1 = input('Sales ')
Credit2 = input('Bank Overdraft ')

Debit = int(Debit1) + int(Debit2)
Credit = int(Credit1) + int(Credit2)

print("The Debit Balance is: ",Debit)
print("The Credit Balance is: ",Credit)
