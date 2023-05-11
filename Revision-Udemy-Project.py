# Printing Excercise
# Instructions Write a program in main.py that prints the same notes from the #previous lesson using what you have learnt about the Python print function.
# Warning: The output in your program should match the example output shown below exactly, character for character, even spaces and symbols should be identical, otherwise the tests won't pass.
# Example Output
# After you have written your code, you should run your program and it should print the following:
# Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.

# Warning: The output in your program should match the example output shown below exactly, character for character, even spaces and symbols should be identical, otherwise the tests won't pass.

# Example Output
# After you have written your code, you should run your program and it should print the following: -->
print("Day -1 Python Print Function")
print("The function is declared like this:")
print("print('what to print')")



# Instructions
# Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.
# Warning: The output in your program should match the example output shown below exactly, character for character, even spaces and symbols should be identical, otherwise the tests won't pass.
# Example Output
# When you run your program, it should print the following:
print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Instructions
# Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.
# e.g.
# https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow
# Warning. Your program should work for different inputs. e.g. any name that you input.
name = (input("what is your name?"))
print(len(name))


# Instructions
# Write a program that switches the values stored in the variables a and b.
# Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = input("c: ")
a,b,c = b,a,c
c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)



#1. Create a greeting for your program.
print("Hello Welcome to NextGenTechnologies")
#2. Ask the user for the city that they grew up in.
city = input("Please type in the name of the city you grew up in?")

#3. Ask the user for the name of a pet.
pet = input("Please enter the name of your pet?")

#4. Combine the name of their city and pet and show them their band name.
brand_name = print(city +  pet ,'\n')
