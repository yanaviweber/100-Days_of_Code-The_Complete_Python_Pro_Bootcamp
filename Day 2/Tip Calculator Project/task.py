# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

#
# 150
#
# 12 / 100 = 0.12

# print(150 * 0.12 + 150) # Output 168.0
# print(150 * 1.12) # Output 168.00000000000003
#
# print(150 * 1.12 / 5)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)
print(f"Each person should pay: $ {final_amount}")

# bill_with_tip = tip / 100 * bill + bill
# bill_with_tip = bill * (1 + tip / 100) # Output the same result as bill_with_tip = tip / 100 * bill + bill
# print(bill_with_tip)