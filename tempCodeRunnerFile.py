print("welcome to the friends tip calculator")
bill = float(input("Enter the bill amount?: "))
people = int(input("Enter the number of people in which bill needs to be divided?: "))
tip = int(input("please select the tip as 12%, 13%,15%?: "))

tip_as_percent = tip/100
amount = bill * tip_as_percent
total_bill = bill + amount
amount_per_person = total_bill /people
final_bill = round(amount_per_person, 2)
print(f"Each person should pay: ${final_bill}")