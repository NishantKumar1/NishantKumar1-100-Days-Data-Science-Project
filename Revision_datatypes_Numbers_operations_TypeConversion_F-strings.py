# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.
two_digit_number = input("Type a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
result = first_digit + second_digit
print(result)


# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Warning you should convert the result to a whole number.



weight = input(" Please enter your weight in Kg ?")
height = input("Please enter your height in cm ?")
w = int(weight)
h= float(height)
BMI = w/h**2
BMI = round(BMI)
print(f"Your BMI is {BMI} ")

# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# https://waitbutwhy.com/2014/05/life-weeks.html

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

age = input("what is your current age ?")
age = int(age)
expected_age = 90
current_age = (expected_age - age)
days= (current_age * 365)
weeks = (current_age*52)
months = (current_age*12)
print(f"You have {days} days,{weeks} weeks,and {months} months left")


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

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


