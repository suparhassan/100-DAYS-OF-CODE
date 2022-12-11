#Day-2 Tip Calculator by supar

welcome_message = "Welcome to the Tip Calculator. by supar\n"
print(welcome_message)

bill_total = float(input("What is the total bill? "))
tip_percentage = int(input("What percentage top would you like to give? 10, 12, or 15? "))
num_of_ppl = int(input("How many people to split the bill? "))

tip_amount = bill_total + bill_total * (tip_percentage / 100)

split_amount = round( tip_amount / (num_of_ppl), 2)

print (f"Each person should pay {split_amount}")


