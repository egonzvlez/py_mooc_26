
"""
Problem 1:
Please write a program which estimates a user's typical food expenditure.
The program asks the user how many times a week they eat at the student cafeteria.
Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.
Based on this information the program calculates the user's typical food expenditure both weekly and daily.
"""

# times_at_cafeteria: int = int(input("How many time a week do you eat at the student cafeteria? "))
# lunch_price: float = float(input("The price of a typical student lunch? "))
# grocerie_weekly: float = float(input("How much money do you spend on groceries in a week? "))

# daily_spending: float = ((times_at_cafeteria * lunch_price) + grocerie_weekly) / 7
# weekly_spending: float = (times_at_cafeteria * lunch_price) + grocerie_weekly
# print("Average food expenditure: ")
# print(f"Daily: {daily_spending} euros")
# print(f"Weekly: {weekly_spending} euros")


""" (Incomplete)
Problem 2:
Please write a program which asks for the number of students on a course and the desired group size. 
The program will then print out the number of groups formed from the students on the course. 
If the division is not even, one of the groups may have fewer members than specified.
"""

# total_students: int = int(input("How many students on the course? "))
# group_size: int = int(input("Desired group size? "))
# number_of_groups: int = total_students / group_size
# if total_students % group_size == 0:
#     print(f"Number of groups formed: {number_of_groups}")
# if total_students % group_size != 0:
#     print(f"Number of groups formed: {number_of_groups  + 1}")


"""
Problem 3:
Please write a program which asks the user for an integer number. 
The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.
"""

# orwell_num: int = int(input("Please type in a number: "))
# if orwell_num == 1984:
#     print("Orwell")


"""
Problem 4:
Please write a program which asks the user for an integer number. 
If the number is less than zero, the program should print out the number multiplied by -1. 
Otherwise the program prints out the number as is. 
Please have a look at the examples of expected behaviour below.
"""

# user_input: int = int(input("Please type in a number: "))
# if user_input < 0:
#     print(f"The absolute value of this number is {user_input * -1}")
# else:
#     print(f"The absolute value of this number is {user_input}")

"""Problem 5:
Please write a program which asks for the user's name. 
If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. 
The price of a single portion is 5.90.
"""

# user_name: str = input("Please tell me your name:")
# cost_per_portion: float = 5.90

# if user_name == "Jerry":
#     print("Next please!")
# else:
#     portions: int = int(input("How many portions of soup: "))
#     total_cost = portions * cost_per_portion
#     print(f"The total cost is {total_cost}")
#     print("Next please!")


"""
Problem 6:
Please write a program which asks the user for an integer number. 
The program should then print out the magnitude of the number according to the following examples.
"""

# user_number: int = int(input("Please type in a number:"))

# if user_number < 1000:
#     print("This number is smaller than 1000")
# if user_number < 100:
#     print("This number is smaller than 100")
# if user_number < 10:
#     print("This number is smaller than 10")

# print("Thank you!")


"""Problem 7
Please write a program which asks the user for two numbers and an operation. 
If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. 
If the user types in anything else, the program should print out nothing.
"""
# operand_one: int = int(input("Number 1:"))
# operand_two: int = int(input("Number 2:"))
# operator: str = input("Operation:")

# if operator == "add":
#     print(f"{operand_one} + {operand_two} = {operand_one + operand_two}")
# if operator == "multiply":
#     print(f"{operand_one} * {operand_two} = {operand_one * operand_two}")
# if operator == "subtract":
#     print(f"{operand_one} - {operand_two} = {operand_one - operand_two}")


"""Problem 8
Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. 
If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".
The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.
"""

# f_temp: int = int(input("Please type in a temperature (F): "))
# conversion_c = (f_temp - 32) * 5/9

# if conversion_c < 0:
#     print(f"{f_temp} degrees Fahrenheit equals {conversion_c} degrees Celsius")
#     print("Brr! It's cold in here!")
# print(f"{f_temp} degrees Fahrenheit equals {conversion_c} degrees Celsius")

"""Problem 9
Please write a program which asks for the hourly wage, hours worked, and the day of the week. 
The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.
"""

# hrly_wage: float = float(input("Hourly wage:" ))
# hrs_worked: int = int(input("Hours worked: "))
# day_of_week: str = input("Day of the week: ")

# daily_wage = hrly_wage * hrs_worked

# if day_of_week == "Sunday":
#     print(f"Daily wages: {daily_wage * 2} euros")
# if day_of_week != "Sunday":
#     print(f"Daily wages: {daily_wage} euros")

"""Problem 10
Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.
The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.
"""

# print("What is the weather forecast tomorrow?")
# temp = int(input("Temperature: "))
# is_raining = input("Will it rain (yes/no): ")

# if temp > 20:
#     print("Wear jeans and a T-shirt")
# elif temp > 10:
#     print("Wear jeans and a T-shirt")
#     print("I recommend a jumper as well")
# elif temp > 5:
#     print("Wear jeans and a T-shirt")
#     print("I recommend a jumper as well")
#     print("Take a jacket with you")
# elif temp <= 5:
#     print("Wear jeans and a T-shirt")
#     print("I recommend a jumper as well")
#     print("Take a jacket with you")
#     print("Make it a warm coat, actually")
#     print("I think gloves are in order")
# if is_raining == "yes":
#     print("Don't forget your umbrella!")

"""Problem 11
Please write a program for solving a quadratic equation of the form ax²+bx+c. 
The program asks for values a, b and c. It should then use the quadratic formula to solve the equation.
The quadratic formula expressed with the Python sqrt function is as follows:
"""
# import math

# a_value: int = int(input("Value of a:"))
# b_value: int = int(input("Value of b:"))
# c_value: int = int(input("Value of c:"))

# root_one: float = (-b_value + math.sqrt(pow(b_value,2) - (4 * a_value * c_value))) / (2 * a_value)
# root_two: float = (-b_value - math.sqrt(pow(b_value,2) - (4 * a_value * c_value))) / (2 * a_value)
# print(f"The roots are {root_one} and {root_two}")


